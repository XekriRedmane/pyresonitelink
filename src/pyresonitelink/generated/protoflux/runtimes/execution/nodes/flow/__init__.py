"""Generated flow components."""

import importlib

from .data_model_boolean_toggle import DataModelBooleanToggle
from .delay_seconds_double import DelaySecondsDouble
from .delay_seconds_float import DelaySecondsFloat
from .delay_seconds_int import DelaySecondsInt
from .delay_time_span import DelayTimeSpan
from .delay_with_object_seconds_double import DelayWithObjectSecondsDouble
from .delay_with_object_seconds_float import DelayWithObjectSecondsFloat
from .delay_with_object_seconds_int import DelayWithObjectSecondsInt
from .delay_with_object_time_span import DelayWithObjectTimeSpan
from .delay_with_value_seconds_double import DelayWithValueSecondsDouble
from .delay_with_value_seconds_float import DelayWithValueSecondsFloat
from .delay_with_value_seconds_int import DelayWithValueSecondsInt
from .delay_with_value_time_span import DelayWithValueTimeSpan
from .dynamic_impulse_receiver import DynamicImpulseReceiver
from .dynamic_impulse_receiver_with_object import DynamicImpulseReceiverWithObject
from .dynamic_impulse_receiver_with_value import DynamicImpulseReceiverWithValue
from .dynamic_impulse_trigger import DynamicImpulseTrigger
from .dynamic_impulse_trigger_with_object import DynamicImpulseTriggerWithObject
from .dynamic_impulse_trigger_with_value import DynamicImpulseTriggerWithValue
from .fire_on_false import FireOnFalse
from .fire_on_local_false import FireOnLocalFalse
from .fire_on_local_object_change import FireOnLocalObjectChange
from .fire_on_local_true import FireOnLocalTrue
from .fire_on_local_value_change import FireOnLocalValueChange
from .fire_on_object_value_change import FireOnObjectValueChange
from .fire_on_ref_change import FireOnRefChange
from .fire_on_true import FireOnTrue
from .fire_on_type_change import FireOnTypeChange
from .fire_on_value_change import FireOnValueChange
from .fire_while_true import FireWhileTrue
For = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.for").For
If = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.if").If
from .impulse_demultiplexer import ImpulseDemultiplexer
from .impulse_multiplexer import ImpulseMultiplexer
from .local_fire_while_true import LocalFireWhileTrue
from .local_impulse_timeout_seconds import LocalImpulseTimeoutSeconds
from .local_impulse_timeout_time_span import LocalImpulseTimeoutTimeSpan
from .local_leaky_impulse_bucket import LocalLeakyImpulseBucket
from .local_update import LocalUpdate
from .one_per_frame import OnePerFrame
from .pulse_random import PulseRandom
from .range_loop_int import RangeLoopInt
from .seconds_timer import SecondsTimer
from .sequence import Sequence
from .update import Update
from .updates_timer import UpdatesTimer
While = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.while").While
AsyncDynamicImpulseReceiver = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_receiver").AsyncDynamicImpulseReceiver
AsyncDynamicImpulseReceiverWithObject = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_receiver_with_object").AsyncDynamicImpulseReceiverWithObject
AsyncDynamicImpulseReceiverWithValue = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_receiver_with_value").AsyncDynamicImpulseReceiverWithValue
AsyncDynamicImpulseTrigger = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_trigger").AsyncDynamicImpulseTrigger
AsyncDynamicImpulseTriggerWithObject = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_trigger_with_object").AsyncDynamicImpulseTriggerWithObject
AsyncDynamicImpulseTriggerWithValue = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_dynamic_impulse_trigger_with_value").AsyncDynamicImpulseTriggerWithValue
AsyncFor = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_for").AsyncFor
AsyncRangeLoopInt = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_range_loop_int").AsyncRangeLoopInt
AsyncSequence = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_sequence").AsyncSequence
AsyncWhile = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.async_while").AsyncWhile
DelayUpdates = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates").DelayUpdates
DelayUpdatesOrSecondsDouble = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_seconds_double").DelayUpdatesOrSecondsDouble
DelayUpdatesOrSecondsFloat = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_seconds_float").DelayUpdatesOrSecondsFloat
DelayUpdatesOrSecondsInt = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_seconds_int").DelayUpdatesOrSecondsInt
DelayUpdatesOrTimeSpan = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_span").DelayUpdatesOrTimeSpan
DelayUpdatesOrTimeWithObjectSecondsDouble = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_object_seconds_double").DelayUpdatesOrTimeWithObjectSecondsDouble
DelayUpdatesOrTimeWithObjectSecondsFloat = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_object_seconds_float").DelayUpdatesOrTimeWithObjectSecondsFloat
DelayUpdatesOrTimeWithObjectSecondsInt = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_object_seconds_int").DelayUpdatesOrTimeWithObjectSecondsInt
DelayUpdatesOrTimeWithObjectTimeSpan = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_object_time_span").DelayUpdatesOrTimeWithObjectTimeSpan
DelayUpdatesOrTimeWithValueSecondsDouble = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_value_seconds_double").DelayUpdatesOrTimeWithValueSecondsDouble
DelayUpdatesOrTimeWithValueSecondsFloat = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_value_seconds_float").DelayUpdatesOrTimeWithValueSecondsFloat
DelayUpdatesOrTimeWithValueSecondsInt = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_value_seconds_int").DelayUpdatesOrTimeWithValueSecondsInt
DelayUpdatesOrTimeWithValueTimeSpan = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_or_time_with_value_time_span").DelayUpdatesOrTimeWithValueTimeSpan
DelayUpdatesWithObject = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_with_object").DelayUpdatesWithObject
DelayUpdatesWithValue = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.delay_updates_with_value").DelayUpdatesWithValue
StartAsyncTask = importlib.import_module("pyresonitelink.generated.protoflux.runtimes.execution.nodes.flow.async.start_async_task").StartAsyncTask
from .events.on_activated import OnActivated
from .events.on_deactivated import OnDeactivated
from .events.on_destroy import OnDestroy
from .events.on_destroying import OnDestroying
from .events.on_duplicate import OnDuplicate
from .events.on_loaded import OnLoaded
from .events.on_package_imported import OnPackageImported
from .events.on_paste import OnPaste
from .events.on_saving import OnSaving
from .events.on_start import OnStart
