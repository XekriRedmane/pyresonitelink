"""Generated component: PlatformInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlatformInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlatformInfo.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlatformInfo"

    def __init__(self, platform_name: str | None = None, short_name_prefix: str | None = None, abbreviation: str | None = None, domain: str | None = None, email: str | None = None, discord_invite_url: str | None = None, policies_page: str | None = None, patreon_url: str | None = None, git_hub_profile: str | None = None, git_hub_issues_repository: str | None = None, auth_scheme: str | None = None, app_scheme: str | None = None, db_scheme: str | None = None, session_scheme: str | None = None, record_scheme: str | None = None, user_session_scheme: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            platform_name: Initial value for PlatformName.
            short_name_prefix: Initial value for ShortNamePrefix.
            abbreviation: Initial value for Abbreviation.
            domain: Initial value for Domain.
            email: Initial value for Email.
            discord_invite_url: Initial value for DiscordInviteUrl.
            policies_page: Initial value for PoliciesPage.
            patreon_url: Initial value for PatreonUrl.
            git_hub_profile: Initial value for GitHubProfile.
            git_hub_issues_repository: Initial value for GitHubIssuesRepository.
            auth_scheme: Initial value for AuthScheme.
            app_scheme: Initial value for AppScheme.
            db_scheme: Initial value for DBScheme.
            session_scheme: Initial value for SessionScheme.
            record_scheme: Initial value for RecordScheme.
            user_session_scheme: Initial value for UserSessionScheme.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if platform_name is not None:
            self.platform_name = platform_name
        if short_name_prefix is not None:
            self.short_name_prefix = short_name_prefix
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if domain is not None:
            self.domain = domain
        if email is not None:
            self.email = email
        if discord_invite_url is not None:
            self.discord_invite_url = discord_invite_url
        if policies_page is not None:
            self.policies_page = policies_page
        if patreon_url is not None:
            self.patreon_url = patreon_url
        if git_hub_profile is not None:
            self.git_hub_profile = git_hub_profile
        if git_hub_issues_repository is not None:
            self.git_hub_issues_repository = git_hub_issues_repository
        if auth_scheme is not None:
            self.auth_scheme = auth_scheme
        if app_scheme is not None:
            self.app_scheme = app_scheme
        if db_scheme is not None:
            self.db_scheme = db_scheme
        if session_scheme is not None:
            self.session_scheme = session_scheme
        if record_scheme is not None:
            self.record_scheme = record_scheme
        if user_session_scheme is not None:
            self.user_session_scheme = user_session_scheme

    @property
    def platform_name(self) -> str | None:
        """The PlatformName field value."""
        member = self.get_member("PlatformName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @platform_name.setter
    def platform_name(self, value: str) -> None:
        """Set the PlatformName field value."""
        member = self.get_member("PlatformName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PlatformName", fields.FieldString(value=value)
            )

    @property
    def short_name_prefix(self) -> str | None:
        """The ShortNamePrefix field value."""
        member = self.get_member("ShortNamePrefix")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @short_name_prefix.setter
    def short_name_prefix(self, value: str) -> None:
        """Set the ShortNamePrefix field value."""
        member = self.get_member("ShortNamePrefix")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShortNamePrefix", fields.FieldString(value=value)
            )

    @property
    def abbreviation(self) -> str | None:
        """The Abbreviation field value."""
        member = self.get_member("Abbreviation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @abbreviation.setter
    def abbreviation(self, value: str) -> None:
        """Set the Abbreviation field value."""
        member = self.get_member("Abbreviation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Abbreviation", fields.FieldString(value=value)
            )

    @property
    def domain(self) -> str | None:
        """The Domain field value."""
        member = self.get_member("Domain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @domain.setter
    def domain(self, value: str) -> None:
        """Set the Domain field value."""
        member = self.get_member("Domain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Domain", fields.FieldString(value=value)
            )

    @property
    def email(self) -> str | None:
        """The Email field value."""
        member = self.get_member("Email")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @email.setter
    def email(self, value: str) -> None:
        """Set the Email field value."""
        member = self.get_member("Email")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Email", fields.FieldString(value=value)
            )

    @property
    def discord_invite_url(self) -> str | None:
        """The DiscordInviteUrl field value."""
        member = self.get_member("DiscordInviteUrl")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @discord_invite_url.setter
    def discord_invite_url(self, value: str) -> None:
        """Set the DiscordInviteUrl field value."""
        member = self.get_member("DiscordInviteUrl")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DiscordInviteUrl", fields.FieldString(value=value)
            )

    @property
    def policies_page(self) -> str | None:
        """The PoliciesPage field value."""
        member = self.get_member("PoliciesPage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @policies_page.setter
    def policies_page(self, value: str) -> None:
        """Set the PoliciesPage field value."""
        member = self.get_member("PoliciesPage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PoliciesPage", fields.FieldString(value=value)
            )

    @property
    def patreon_url(self) -> str | None:
        """The PatreonUrl field value."""
        member = self.get_member("PatreonUrl")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @patreon_url.setter
    def patreon_url(self, value: str) -> None:
        """Set the PatreonUrl field value."""
        member = self.get_member("PatreonUrl")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PatreonUrl", fields.FieldString(value=value)
            )

    @property
    def git_hub_profile(self) -> str | None:
        """The GitHubProfile field value."""
        member = self.get_member("GitHubProfile")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @git_hub_profile.setter
    def git_hub_profile(self, value: str) -> None:
        """Set the GitHubProfile field value."""
        member = self.get_member("GitHubProfile")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GitHubProfile", fields.FieldString(value=value)
            )

    @property
    def git_hub_issues_repository(self) -> str | None:
        """The GitHubIssuesRepository field value."""
        member = self.get_member("GitHubIssuesRepository")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @git_hub_issues_repository.setter
    def git_hub_issues_repository(self, value: str) -> None:
        """Set the GitHubIssuesRepository field value."""
        member = self.get_member("GitHubIssuesRepository")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GitHubIssuesRepository", fields.FieldString(value=value)
            )

    @property
    def auth_scheme(self) -> str | None:
        """The AuthScheme field value."""
        member = self.get_member("AuthScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auth_scheme.setter
    def auth_scheme(self, value: str) -> None:
        """Set the AuthScheme field value."""
        member = self.get_member("AuthScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AuthScheme", fields.FieldString(value=value)
            )

    @property
    def app_scheme(self) -> str | None:
        """The AppScheme field value."""
        member = self.get_member("AppScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @app_scheme.setter
    def app_scheme(self, value: str) -> None:
        """Set the AppScheme field value."""
        member = self.get_member("AppScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppScheme", fields.FieldString(value=value)
            )

    @property
    def db_scheme(self) -> str | None:
        """The DBScheme field value."""
        member = self.get_member("DBScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @db_scheme.setter
    def db_scheme(self, value: str) -> None:
        """Set the DBScheme field value."""
        member = self.get_member("DBScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DBScheme", fields.FieldString(value=value)
            )

    @property
    def session_scheme(self) -> str | None:
        """The SessionScheme field value."""
        member = self.get_member("SessionScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @session_scheme.setter
    def session_scheme(self, value: str) -> None:
        """Set the SessionScheme field value."""
        member = self.get_member("SessionScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SessionScheme", fields.FieldString(value=value)
            )

    @property
    def record_scheme(self) -> str | None:
        """The RecordScheme field value."""
        member = self.get_member("RecordScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @record_scheme.setter
    def record_scheme(self, value: str) -> None:
        """Set the RecordScheme field value."""
        member = self.get_member("RecordScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RecordScheme", fields.FieldString(value=value)
            )

    @property
    def user_session_scheme(self) -> str | None:
        """The UserSessionScheme field value."""
        member = self.get_member("UserSessionScheme")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_session_scheme.setter
    def user_session_scheme(self, value: str) -> None:
        """Set the UserSessionScheme field value."""
        member = self.get_member("UserSessionScheme")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserSessionScheme", fields.FieldString(value=value)
            )

