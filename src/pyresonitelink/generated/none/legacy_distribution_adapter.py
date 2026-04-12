"""Generated component: LegacyDistributionAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.particle_follower_distribution import ParticleFollowerDistribution
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyDistributionAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyDistributionAdapter is used in converted legacy particle systems that were converted to PhotonDust as part of The Performance Updates.

    Not used by the user. auto generated.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyDistributionAdapter"

    def __init__(self, use_random_distribution: primitives.Bool | None = None, distribution: str | IField[ParticleFollowerDistribution] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_random_distribution: Initial value for UseRandomDistribution.
            distribution: Initial value for Distribution.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_random_distribution is not None:
            self.use_random_distribution = use_random_distribution
        if distribution is not None:
            self.distribution = distribution

    @property
    def use_random_distribution(self) -> primitives.Bool | None:
        """The value to convert."""
        member = self.get_member("UseRandomDistribution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_random_distribution.setter
    def use_random_distribution(self, value: primitives.Bool) -> None:
        """Set the UseRandomDistribution field value."""
        member = self.get_member("UseRandomDistribution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseRandomDistribution", fields.FieldBool(value=value)
            )

    @property
    def distribution(self) -> str | None:
        """The field to drive with ``UseRandomDistibution`` converted."""
        member = self.get_member("Distribution")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distribution.setter
    def distribution(self, target: str | IField[ParticleFollowerDistribution] | None) -> None:
        """Set the Distribution reference by target ID or IField[ParticleFollowerDistribution] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Distribution")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Distribution",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.ParticleFollowerDistribution>'),
            )

