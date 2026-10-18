"""TUI app for displaying Resonite slot hierarchy as an interactive tree."""

import argparse

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle
from textual.widgets import Header, Label, LoadingIndicator, Static, Tree
from textual.widgets.tree import TreeNode

from pyresonitelink import client
from pyresonitelink.data import messages, responses
from pyresonitelink.data.workers import Slot


class SlotTreeApp(App):
    """A Textual app to display and navigate the Resonite slot hierarchy."""

    TITLE = "Resonite Slot Tree"
    CSS = """
    Tree {
        scrollbar-gutter: stable;
    }

    #loading-container {
        width: 100%;
        height: 100%;
    }

    #loading-label {
        text-style: bold;
        margin-bottom: 1;
    }

    #footer {
        dock: bottom;
        height: 1;
        background: $secondary;
        color: $text;
    }
    """

    BINDINGS = [
        Binding("up", "cursor_up", "Up", key_display="↑"),
        Binding("down", "cursor_down", "Down", key_display="↓"),
        Binding("space", "toggle_node", "Toggle", key_display="Space"),
        Binding("enter", "toggle_node", "Toggle", show=False),
        Binding("c", "collapse_all", "Collapse All"),
        Binding("q", "quit", "Quit"),
    ]

    def __init__(self, port: int, host: str = "localhost"):
        super().__init__()
        self.port = port
        self.host = host
        self.resolink: client.Client | None = None
        self.root_slot: Slot | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        with Middle(id="loading-container"):
            with Center():
                yield Label("Connecting to Resonite...", id="loading-label")
                yield LoadingIndicator()
        yield Tree("Root")
        yield Static(
            " [b]↑[/b] Up  [b]↓[/b] Down  [b]Space[/b] Toggle  "
            "[b]c[/b] Collapse All  [b]q[/b] Quit ",
            id="footer",
        )

    def on_mount(self) -> None:
        """Hide the tree initially and start loading."""
        tree = self.query_one(Tree)
        tree.display = False
        self.run_worker(self._load_data(), exclusive=True)

    async def _load_data(self) -> None:
        """Connect to Resonite and fetch the root slot."""
        tree = self.query_one(Tree)
        loading_container = self.query_one("#loading-container")
        loading_label = self.query_one("#loading-label", Label)

        try:
            loading_label.update("Connecting to Resonite...")
            self.resolink = client.Client()
            await self.resolink.connect(self.port, self.host)

            loading_label.update("Loading slot hierarchy...")

            response = await self.resolink.request(
                messages.GetSlot(
                    slotId=Slot.ROOT_SLOT_ID, depth=-1, includeComponentData=False
                )
            )

            if (
                response.success
                and isinstance(response, responses.SlotData)
                and response.data
            ):
                loading_label.update("Building tree...")
                self.root_slot = response.data
                tree.show_root = True
                self._build_tree(tree, response.data)

                # Hide loading, show tree
                loading_container.display = False
                tree.display = True
            else:
                error_msg = getattr(response, "errorInfo", None) or "Unknown error"
                loading_label.update(f"Error: {error_msg}")

        except Exception as e:
            loading_label.update(f"Connection failed: {e}")

    def _build_tree(self, tree: Tree, root_slot: Slot) -> None:
        """Build the tree widget from slot data."""
        tree.root.set_label(self._get_slot_name(root_slot))
        tree.root.data = root_slot

        # Add children recursively
        self._add_slot_children(tree.root, root_slot)

        # Collapse the root initially
        tree.root.collapse()

    def _get_slot_name(self, slot: Slot) -> str:
        """Get the display name for a slot."""
        if slot.name and slot.name.value:
            return slot.name.value
        return "(unnamed)"

    def _add_slot_children(self, node: TreeNode, slot: Slot) -> None:
        """Recursively add child slots to a tree node."""
        if not slot.children:
            return
        for child in slot.children:
            child_name = self._get_slot_name(child)
            if child.children:
                # Has children - add as expandable node
                child_node = node.add(child_name, data=child)
                self._add_slot_children(child_node, child)
                child_node.collapse()
            else:
                # No children - add as leaf
                node.add_leaf(child_name, data=child)

    def action_collapse_all(self) -> None:
        """Collapse all nodes in the tree."""
        tree = self.query_one(Tree)

        def collapse_recursive(node: TreeNode) -> None:
            node.collapse()
            for child in node.children:
                collapse_recursive(child)

        collapse_recursive(tree.root)

    def action_toggle_node(self) -> None:
        """Toggle expansion of the currently selected node."""
        tree = self.query_one(Tree)
        if tree.cursor_node:
            tree.cursor_node.toggle()

    async def on_unmount(self) -> None:
        """Close the connection when the app exits."""
        if self.resolink:
            await self.resolink.close()


def main() -> None:
    """Run the slot tree TUI app."""
    parser = argparse.ArgumentParser(
        description="Display Resonite slot hierarchy as an interactive tree"
    )
    parser.add_argument(
        "port", type=int, help="Port number for ResoniteLink connection"
    )
    parser.add_argument(
        "--host", default="localhost", help="Host address (default: localhost)"
    )

    args = parser.parse_args()

    app = SlotTreeApp(args.port, args.host)
    app.run()


if __name__ == "__main__":
    main()
