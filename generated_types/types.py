from typing_extensions import Self
from typing import Any, Callable, Literal
from abc import abstractmethod
from enum import Enum
from functools import singledispatchmethod

class Vector3:
	pass

class CFrame:
	pass

class Content:
	pass

class Color3:
	pass

class BrickColor:
	pass

class ColorSequence:
	pass

class NumberSequence:
	pass

class Vector2:
	pass

class Font:
	pass

class Rect:
	pass

class UDim2:
	pass

class Axes:
	pass

class Faces:
	pass

class ProtectedString:
	pass

class PhysicalProperties:
	pass

class Ray:
	pass

class BinaryString:
	pass

class Region3int16:
	pass

class NumberRange:
	pass

class QDir:
	pass

class QFont:
	pass

class DateTime:
	pass

class TweenInfo:
	pass

class UDim:
	pass

class RBXScriptSignal:
	pass

class CatalogSearchParams:
	pass

class FloatCurveKey:
	pass

class RBXScriptConnection:
	pass

class Region3:
	pass

class Map:
	pass

class Vector3int16:
	pass

class OverlapParams:
	pass

class RaycastResult:
	pass

class RaycastParams:
	pass

class DockWidgetPluginGuiInfo:
	pass

class RotationCurveKey:
	pass

class CoordinateFrame:
	pass

class AccessoryType(Enum):
	Unknown = 0
	Hat = 1
	Hair = 2
	Face = 3
	Neck = 4
	Shoulder = 5
	Front = 6
	Back = 7
	Waist = 8
	TShirt = 9
	Shirt = 10
	Pants = 11
	Jacket = 12
	Sweater = 13
	Shorts = 14
	LeftShoe = 15
	RightShoe = 16
	DressSkirt = 17
	Eyebrow = 18
	Eyelash = 19
	pass

class ActionType(Enum):
	Nothing = 0
	Pause = 1
	Lose = 2
	Draw = 3
	Win = 4
	pass

class ActuatorRelativeTo(Enum):
	Attachment0 = 0
	Attachment1 = 1
	World = 2
	pass

class ActuatorType(Enum):
	NONE = 0
	Motor = 1
	Servo = 2
	pass

class AdPortalStatus(Enum):
	Invalid = 0
	Inactive = 1
	Active = 2
	pass

class AdPortalType(Enum):
	Forward = 0
	Return = 1
	pass

class AdShape(Enum):
	HorizontalRectangle = 1
	pass

class AdornCullingMode(Enum):
	Automatic = 0
	Never = 1
	pass

class AlignType(Enum):
	Parallel = 0
	Perpendicular = 1
	pass

class AlphaMode(Enum):
	Overlay = 0
	Transparency = 1
	pass

class AnalyticsEconomyAction(Enum):
	Default = 0
	Acquire = 1
	Spend = 2
	pass

class AnalyticsLogLevel(Enum):
	Trace = 0
	Debug = 1
	Information = 2
	Warning = 3
	Error = 4
	Fatal = 5
	pass

class AnalyticsProgressionStatus(Enum):
	Default = 0
	Begin = 1
	Complete = 2
	Abandon = 3
	Fail = 4
	pass

class AnimationPriority(Enum):
	Idle = 0
	Movement = 1
	Action = 2
	Action2 = 3
	Action3 = 4
	Action4 = 5
	Core = 1000
	pass

class AnimatorRetargetingMode(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class AppShellActionType(Enum):
	NONE = 0
	OpenApp = 1
	TapChatTab = 2
	TapConversationEntry = 3
	TapAvatarTab = 4
	ReadConversation = 5
	TapGamePageTab = 6
	TapHomePageTab = 7
	GamePageLoaded = 8
	HomePageLoaded = 9
	AvatarEditorPageLoaded = 10
	pass

class AppShellFeature(Enum):
	NONE = 0
	Chat = 1
	AvatarEditor = 2
	GamePage = 3
	HomePage = 4
	More = 5
	Landing = 6
	pass

class AppUpdateStatus(Enum):
	Unknown = 0
	NotSupported = 1
	Failed = 2
	NotAvailable = 3
	Available = 4
	pass

class ApplyStrokeMode(Enum):
	Contextual = 0
	Border = 1
	pass

class AspectType(Enum):
	FitWithinMaxSize = 0
	ScaleWithParentSize = 1
	pass

class AssetFetchStatus(Enum):
	Success = 0
	Failure = 1
	pass

class AssetType(Enum):
	Image = 1
	TShirt = 2
	Audio = 3
	Mesh = 4
	Lua = 5
	Hat = 8
	Place = 9
	Model = 10
	Shirt = 11
	Pants = 12
	Decal = 13
	Head = 17
	Face = 18
	Gear = 19
	Badge = 21
	Animation = 24
	Torso = 27
	RightArm = 28
	LeftArm = 29
	LeftLeg = 30
	RightLeg = 31
	Package = 32
	GamePass = 34
	Plugin = 38
	MeshPart = 40
	HairAccessory = 41
	FaceAccessory = 42
	NeckAccessory = 43
	ShoulderAccessory = 44
	FrontAccessory = 45
	BackAccessory = 46
	WaistAccessory = 47
	ClimbAnimation = 48
	DeathAnimation = 49
	FallAnimation = 50
	IdleAnimation = 51
	JumpAnimation = 52
	RunAnimation = 53
	SwimAnimation = 54
	WalkAnimation = 55
	PoseAnimation = 56
	MoodAnimation = 78
	EarAccessory = 57
	EyeAccessory = 58
	EmoteAnimation = 61
	Video = 62
	TShirtAccessory = 64
	ShirtAccessory = 65
	PantsAccessory = 66
	JacketAccessory = 67
	SweaterAccessory = 68
	ShortsAccessory = 69
	LeftShoeAccessory = 70
	RightShoeAccessory = 71
	DressSkirtAccessory = 72
	EyebrowAccessory = 76
	EyelashAccessory = 77
	DynamicHead = 79
	pass

class AssetTypeVerification(Enum):
	Default = 1
	ClientOnly = 2
	Always = 3
	pass

class AutoIndentRule(Enum):
	Off = 0
	Absolute = 1
	Relative = 2
	pass

class AutomaticSize(Enum):
	NONE = 0
	X = 1
	Y = 2
	XY = 3
	pass

class AvatarAssetType(Enum):
	TShirt = 2
	Hat = 8
	HairAccessory = 41
	FaceAccessory = 42
	NeckAccessory = 43
	ShoulderAccessory = 44
	FrontAccessory = 45
	BackAccessory = 46
	WaistAccessory = 47
	Shirt = 11
	Pants = 12
	Gear = 19
	Head = 17
	Face = 18
	Torso = 27
	RightArm = 28
	LeftArm = 29
	LeftLeg = 30
	RightLeg = 31
	ClimbAnimation = 48
	FallAnimation = 50
	IdleAnimation = 51
	JumpAnimation = 52
	RunAnimation = 53
	SwimAnimation = 54
	WalkAnimation = 55
	MoodAnimation = 78
	EmoteAnimation = 61
	TShirtAccessory = 64
	ShirtAccessory = 65
	PantsAccessory = 66
	JacketAccessory = 67
	SweaterAccessory = 68
	ShortsAccessory = 69
	LeftShoeAccessory = 70
	RightShoeAccessory = 71
	DressSkirtAccessory = 72
	EyebrowAccessory = 76
	EyelashAccessory = 77
	DynamicHead = 79
	pass

class AvatarContextMenuOption(Enum):
	Friend = 0
	Chat = 1
	Emote = 2
	InspectMenu = 3
	pass

class AvatarItemType(Enum):
	Asset = 1
	Bundle = 2
	pass

class AvatarPromptResult(Enum):
	Success = 1
	PermissionDenied = 2
	Failed = 3
	pass

class Axis(Enum):
	X = 0
	Y = 1
	Z = 2
	pass

class BinType(Enum):
	Script = 0
	GameTool = 1
	Grab = 2
	Clone = 3
	Hammer = 4
	pass

class BodyPart(Enum):
	Head = 0
	Torso = 1
	LeftArm = 2
	RightArm = 3
	LeftLeg = 4
	RightLeg = 5
	pass

class BodyPartR15(Enum):
	Head = 0
	UpperTorso = 1
	LowerTorso = 2
	LeftFoot = 3
	LeftLowerLeg = 4
	LeftUpperLeg = 5
	RightFoot = 6
	RightLowerLeg = 7
	RightUpperLeg = 8
	LeftHand = 9
	LeftLowerArm = 10
	LeftUpperArm = 11
	RightHand = 12
	RightLowerArm = 13
	RightUpperArm = 14
	RootPart = 15
	Unknown = 17
	pass

class BorderMode(Enum):
	Outline = 0
	Middle = 1
	Inset = 2
	pass

class BreakReason(Enum):
	Other = 0
	Error = 1
	UserBreakpoint = 3
	SpecialBreakpoint = 2
	pass

class BreakpointRemoveReason(Enum):
	Requested = 0
	ScriptChanged = 1
	ScriptRemoved = 2
	pass

class BulkMoveMode(Enum):
	FireAllEvents = 0
	FireCFrameChanged = 1
	pass

class BundleType(Enum):
	BodyParts = 1
	Animations = 2
	Shoes = 3
	DynamicHead = 4
	DynamicHeadAvatar = 5
	pass

class Button(Enum):
	Jump = 32
	Dismount = 8
	pass

class ButtonStyle(Enum):
	Custom = 0
	RobloxButtonDefault = 1
	RobloxButton = 2
	RobloxRoundButton = 3
	RobloxRoundDefaultButton = 4
	RobloxRoundDropdownButton = 5
	pass

class CageType(Enum):
	Inner = 0
	Outer = 1
	pass

class CameraMode(Enum):
	Classic = 0
	LockFirstPerson = 1
	pass

class CameraPanMode(Enum):
	Classic = 0
	EdgeBump = 1
	pass

class CameraType(Enum):
	Fixed = 0
	Watch = 2
	Attach = 1
	Track = 3
	Follow = 4
	Custom = 5
	Scriptable = 6
	Orbital = 7
	pass

class CatalogCategoryFilter(Enum):
	NONE = 1
	Featured = 2
	Collectibles = 3
	CommunityCreations = 4
	Premium = 5
	Recommended = 6
	pass

class CatalogSortType(Enum):
	Relevance = 1
	PriceHighToLow = 2
	PriceLowToHigh = 3
	RecentlyUpdated = 4
	MostFavorited = 5
	pass

class CellBlock(Enum):
	Solid = 0
	VerticalWedge = 1
	CornerWedge = 2
	InverseCornerWedge = 3
	HorizontalWedge = 4
	pass

class CellMaterial(Enum):
	Empty = 0
	Grass = 1
	Sand = 2
	Brick = 3
	Granite = 4
	Asphalt = 5
	Iron = 6
	Aluminum = 7
	Gold = 8
	WoodPlank = 9
	WoodLog = 10
	Gravel = 11
	CinderBlock = 12
	MossyStone = 13
	Cement = 14
	RedPlastic = 15
	BluePlastic = 16
	Water = 17
	pass

class CellOrientation(Enum):
	NegZ = 0
	X = 1
	Z = 2
	NegX = 3
	pass

class CenterDialogType(Enum):
	UnsolicitedDialog = 1
	PlayerInitiatedDialog = 2
	ModalDialog = 3
	QuitDialog = 4
	pass

class ChatCallbackType(Enum):
	OnCreatingChatWindow = 1
	OnClientSendingMessage = 2
	OnClientFormattingMessage = 3
	OnServerReceivingMessage = 17
	pass

class ChatColor(Enum):
	Blue = 0
	Green = 1
	Red = 2
	White = 3
	pass

class ChatMode(Enum):
	Menu = 0
	TextAndMenu = 1
	pass

class ChatPrivacyMode(Enum):
	AllUsers = 0
	NoOne = 1
	Friends = 2
	pass

class ChatStyle(Enum):
	Classic = 0
	Bubble = 1
	ClassicAndBubble = 2
	pass

class ChatVersion(Enum):
	LegacyChatService = 0
	TextChatService = 1
	pass

class ClientAnimatorThrottlingMode(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class CollisionFidelity(Enum):
	Default = 0
	Hull = 1
	Box = 2
	PreciseConvexDecomposition = 3
	DynamicPreciseConvexDecomposition = 4
	pass

class CommandPermission(Enum):
	Plugin = 0
	LocalUser = 1
	pass

class CompletionItemKind(Enum):
	Text = 1
	Method = 2
	Function = 3
	Constructor = 4
	Field = 5
	Variable = 6
	Class = 7
	Interface = 8
	Module = 9
	Property = 10
	Unit = 11
	Value = 12
	Enum = 13
	Keyword = 14
	Snippet = 15
	Color = 16
	File = 17
	Reference = 18
	Folder = 19
	EnumMember = 20
	Constant = 21
	Struct = 22
	Event = 23
	Operator = 24
	TypeParameter = 25
	pass

class CompletionItemTag(Enum):
	Deprecated = 1
	IncorrectIndexType = 2
	PluginPermissions = 3
	CommandLinePermissions = 4
	RobloxPermissions = 5
	AddParens = 6
	PutCursorInParens = 7
	TypeCorrect = 8
	ClientServerBoundaryViolation = 9
	pass

class CompletionTriggerKind(Enum):
	Invoked = 1
	TriggerCharacter = 2
	TriggerForIncompleteCompletions = 3
	pass

class ComputerCameraMovementMode(Enum):
	Default = 0
	Follow = 2
	Classic = 1
	Orbital = 3
	CameraToggle = 4
	pass

class ComputerMovementMode(Enum):
	Default = 0
	KeyboardMouse = 1
	ClickToMove = 2
	pass

class ConnectionError(Enum):
	OK = 0
	Unknown = 1
	DisconnectErrors = 256
	DisconnectBadhash = 257
	DisconnectSecurityKeyMismatch = 258
	DisconnectNewSecurityKeyMismatch = 272
	DisconnectProtocolMismatch = 259
	DisconnectReceivePacketError = 260
	DisconnectReceivePacketStreamError = 261
	DisconnectSendPacketError = 262
	DisconnectIllegalTeleport = 263
	DisconnectDuplicatePlayer = 264
	DisconnectDuplicateTicket = 265
	DisconnectTimeout = 266
	DisconnectLuaKick = 267
	DisconnectOnRemoteSysStats = 268
	DisconnectHashTimeout = 269
	DisconnectCloudEditKick = 270
	DisconnectPlayerless = 271
	DisconnectEvicted = 273
	DisconnectDevMaintenance = 274
	DisconnectRobloxMaintenance = 275
	DisconnectRejoin = 276
	DisconnectConnectionLost = 277
	DisconnectIdle = 278
	DisconnectRaknetErrors = 279
	DisconnectWrongVersion = 280
	DisconnectBySecurityPolicy = 281
	DisconnectBlockedIP = 282
	DisconnectClientFailure = 284
	DisconnectClientRequest = 285
	DisconnectOutOfMemory = 286
	DisconnectModeratedGame = 287
	DisconnectOutOfMemoryExitContinue = 288
	DisconnectOutOfMemoryKeepPlayingExit = 289
	PlacelaunchErrors = 512
	PlacelaunchDisabled = 515
	PlacelaunchError = 516
	PlacelaunchGameEnded = 517
	PlacelaunchGameFull = 518
	PlacelaunchUserLeft = 522
	PlacelaunchRestricted = 523
	PlacelaunchUnauthorized = 524
	PlacelaunchFlooded = 525
	PlacelaunchHashExpired = 526
	PlacelaunchHashException = 527
	PlacelaunchPartyCannotFit = 528
	PlacelaunchHttpError = 529
	PlacelaunchUserPrivacyUnauthorized = 533
	PlacelaunchCustomMessage = 610
	PlacelaunchOtherError = 611
	TeleportErrors = 768
	TeleportFailure = 769
	TeleportGameNotFound = 770
	TeleportGameEnded = 771
	TeleportGameFull = 772
	TeleportUnauthorized = 773
	TeleportFlooded = 774
	TeleportIsTeleporting = 775
	pass

class ConnectionState(Enum):
	Connected = 0
	Disconnected = 1
	pass

class ContextActionPriority(Enum):
	Low = 1000
	Medium = 2000
	High = 3000
	pass

class ContextActionResult(Enum):
	Pass = 1
	Sink = 0
	pass

class ControlMode(Enum):
	MouseLockSwitch = 1
	Classic = 0
	pass

class CoreGuiType(Enum):
	PlayerList = 0
	Health = 1
	Backpack = 2
	Chat = 3
	All = 4
	EmotesMenu = 5
	SelfView = 6
	pass

class CreateOutfitFailure(Enum):
	InvalidName = 1
	OutfitLimitReached = 2
	Other = 3
	pass

class CreatorType(Enum):
	User = 0
	Group = 1
	pass

class CurrencyType(Enum):
	Default = 0
	Robux = 1
	Tix = 2
	pass

class CustomCameraMode(Enum):
	Default = 0
	Follow = 2
	Classic = 1
	pass

class DataStoreRequestType(Enum):
	GetAsync = 0
	SetIncrementAsync = 1
	UpdateAsync = 2
	GetSortedAsync = 3
	SetIncrementSortedAsync = 4
	OnUpdate = 5
	pass

class DebuggerEndReason(Enum):
	ClientRequest = 0
	Timeout = 1
	InvalidHost = 2
	Disconnected = 3
	ServerShutdown = 4
	ServerProtocolMismatch = 5
	ConfigurationFailed = 6
	RpcError = 7
	pass

class DebuggerExceptionBreakMode(Enum):
	Never = 0
	Unhandled = 2
	Always = 1
	pass

class DebuggerFrameType(Enum):
	C = 0
	Lua = 1
	pass

class DebuggerPauseReason(Enum):
	Unknown = 0
	Requested = 1
	Breakpoint = 2
	Exception = 3
	SingleStep = 4
	Entrypoint = 5
	pass

class DebuggerStatus(Enum):
	Success = 0
	Timeout = 1
	ConnectionLost = 2
	InvalidResponse = 3
	InternalError = 4
	InvalidState = 5
	RpcError = 6
	InvalidArgument = 7
	ConnectionClosed = 8
	pass

class DevCameraOcclusionMode(Enum):
	Zoom = 0
	Invisicam = 1
	pass

class DevComputerCameraMovementMode(Enum):
	UserChoice = 0
	Classic = 1
	Follow = 2
	Orbital = 3
	CameraToggle = 4
	pass

class DevComputerMovementMode(Enum):
	UserChoice = 0
	KeyboardMouse = 1
	ClickToMove = 2
	Scriptable = 3
	pass

class DevTouchCameraMovementMode(Enum):
	UserChoice = 0
	Classic = 1
	Follow = 2
	Orbital = 3
	pass

class DevTouchMovementMode(Enum):
	UserChoice = 0
	Thumbstick = 1
	DPad = 2
	Thumbpad = 3
	ClickToMove = 4
	Scriptable = 5
	DynamicThumbstick = 6
	pass

class DeveloperMemoryTag(Enum):
	Internal = 0
	HttpCache = 1
	Instances = 2
	Signals = 3
	LuaHeap = 4
	Script = 5
	PhysicsCollision = 6
	PhysicsParts = 7
	GraphicsSolidModels = 8
	GraphicsMeshParts = 10
	GraphicsParticles = 11
	GraphicsParts = 12
	GraphicsSpatialHash = 13
	GraphicsTerrain = 14
	GraphicsTexture = 15
	GraphicsTextureCharacter = 16
	Sounds = 17
	StreamingSounds = 18
	TerrainVoxels = 19
	Gui = 21
	Animation = 22
	Navigation = 23
	GeometryCSG = 24
	pass

class DeviceType(Enum):
	Unknown = 0
	Desktop = 1
	Tablet = 2
	Phone = 3
	pass

class DialogBehaviorType(Enum):
	SinglePlayer = 0
	MultiplePlayers = 1
	pass

class DialogPurpose(Enum):
	Quest = 0
	Help = 1
	Shop = 2
	pass

class DialogTone(Enum):
	Neutral = 0
	Friendly = 1
	Enemy = 2
	pass

class DominantAxis(Enum):
	Width = 0
	Height = 1
	pass

class DraftStatusCode(Enum):
	OK = 0
	DraftOutdated = 1
	ScriptRemoved = 2
	DraftCommitted = 3
	pass

class DraggerCoordinateSpace(Enum):
	Object = 0
	World = 1
	pass

class DraggerMovementMode(Enum):
	Geometric = 0
	Physical = 1
	pass

class EasingDirection(Enum):
	In = 0
	Out = 1
	InOut = 2
	pass

class EasingStyle(Enum):
	Linear = 0
	Sine = 1
	Back = 2
	Quad = 3
	Quart = 4
	Quint = 5
	Bounce = 6
	Elastic = 7
	Exponential = 8
	Circular = 9
	Cubic = 10
	pass

class ElasticBehavior(Enum):
	WhenScrollable = 0
	Always = 1
	Never = 2
	pass

class EnviromentalPhysicsThrottle(Enum):
	DefaultAuto = 0
	Disabled = 1
	Always = 2
	Skip2 = 3
	Skip4 = 4
	Skip8 = 5
	Skip16 = 6
	pass

class ExplosionType(Enum):
	NoCraters = 0
	Craters = 1
	pass

class FacialAnimationFlags(Enum):
	NONE = 0
	Place = 1
	Server = 2
	PlaceServer = 3
	pass

class FacialAnimationStreamingState(Enum):
	NONE = 0
	Audio = 1
	Video = 2
	Place = 4
	Server = 8
	pass

class FieldOfViewMode(Enum):
	Vertical = 0
	Diagonal = 1
	MaxAxis = 2
	pass

class FillDirection(Enum):
	Horizontal = 0
	Vertical = 1
	pass

class FilterResult(Enum):
	Rejected = 1
	Accepted = 0
	pass

class FONT(Enum):
	Legacy = 0
	Arial = 1
	ArialBold = 2
	SourceSans = 3
	SourceSansBold = 4
	SourceSansSemibold = 16
	SourceSansLight = 5
	SourceSansItalic = 6
	Bodoni = 7
	Garamond = 8
	Cartoon = 9
	Code = 10
	Highway = 11
	SciFi = 12
	Arcade = 13
	Fantasy = 14
	Antique = 15
	Gotham = 17
	GothamMedium = 18
	GothamBold = 19
	GothamBlack = 20
	AmaticSC = 21
	Bangers = 22
	Creepster = 23
	DenkOne = 24
	Fondamento = 25
	FredokaOne = 26
	GrenzeGotisch = 27
	IndieFlower = 28
	JosefinSans = 29
	Jura = 30
	Kalam = 31
	LuckiestGuy = 32
	Merriweather = 33
	Michroma = 34
	Nunito = 35
	Oswald = 36
	PatrickHand = 37
	PermanentMarker = 38
	Roboto = 39
	RobotoCondensed = 40
	RobotoMono = 41
	Sarpanch = 42
	SpecialElite = 43
	TitilliumWeb = 44
	Ubuntu = 45
	Unknown = 100
	pass

class FontSize(Enum):
	Size8 = 0
	Size9 = 1
	Size10 = 2
	Size11 = 3
	Size12 = 4
	Size14 = 5
	Size18 = 6
	Size24 = 7
	Size36 = 8
	Size48 = 9
	Size28 = 10
	Size32 = 11
	Size42 = 12
	Size60 = 13
	Size96 = 14
	pass

class FontStyle(Enum):
	Normal = 0
	Italic = 1
	pass

class FontWeight(Enum):
	Thin = 100
	ExtraLight = 200
	Light = 300
	Regular = 400
	Medium = 500
	SemiBold = 600
	Bold = 700
	ExtraBold = 800
	Heavy = 900
	pass

class FormFactor(Enum):
	Symmetric = 0
	Brick = 1
	Plate = 2
	Custom = 3
	pass

class FrameStyle(Enum):
	Custom = 0
	ChatBlue = 1
	RobloxSquare = 2
	RobloxRound = 3
	ChatGreen = 4
	ChatRed = 5
	DropShadow = 6
	pass

class FramerateManagerMode(Enum):
	Automatic = 0
	On = 1
	Off = 2
	pass

class FriendRequestEvent(Enum):
	Issue = 0
	Revoke = 1
	Accept = 2
	Deny = 3
	pass

class FriendStatus(Enum):
	Unknown = 0
	NotFriend = 1
	Friend = 2
	FriendRequestSent = 3
	FriendRequestReceived = 4
	pass

class FunctionalTestResult(Enum):
	Passed = 0
	Warning = 1
	Error = 2
	pass

class GameAvatarType(Enum):
	R6 = 0
	R15 = 1
	PlayerChoice = 2
	pass

class GearGenreSetting(Enum):
	AllGenres = 0
	MatchingGenreOnly = 1
	pass

class GearType(Enum):
	MeleeWeapons = 0
	RangedWeapons = 1
	Explosives = 2
	PowerUps = 3
	NavigationEnhancers = 4
	MusicalInstruments = 5
	SocialItems = 6
	BuildingTools = 7
	Transport = 8
	pass

class Genre(Enum):
	All = 0
	TownAndCity = 1
	Fantasy = 2
	SciFi = 3
	Ninja = 4
	Scary = 5
	Pirate = 6
	Adventure = 7
	Sports = 8
	Funny = 9
	WildWest = 10
	War = 11
	SkatePark = 12
	Tutorial = 13
	pass

class GraphicsMode(Enum):
	Automatic = 1
	Direct3D11 = 2
	OpenGL = 4
	Metal = 5
	Vulkan = 6
	NoGraphics = 7
	pass

class GuiType(Enum):
	Core = 0
	Custom = 1
	CustomBillboards = 3
	PlayerNameplates = 2
	pass

class HandlesStyle(Enum):
	Resize = 0
	Movement = 1
	pass

class HighlightDepthMode(Enum):
	AlwaysOnTop = 0
	Occluded = 1
	pass

class HorizontalAlignment(Enum):
	Center = 0
	Left = 1
	Right = 2
	pass

class HoverAnimateSpeed(Enum):
	VerySlow = 0
	Slow = 1
	Medium = 2
	Fast = 3
	VeryFast = 4
	pass

class HttpCachePolicy(Enum):
	NONE = 0
	Full = 1
	DataOnly = 2
	Default = 3
	InternalRedirectRefresh = 4
	pass

class HttpContentType(Enum):
	ApplicationJson = 0
	ApplicationXml = 1
	ApplicationUrlEncoded = 2
	TextPlain = 3
	TextXml = 4
	pass

class HttpError(Enum):
	OK = 0
	InvalidUrl = 1
	DnsResolve = 2
	ConnectFail = 3
	OutOfMemory = 4
	TimedOut = 5
	TooManyRedirects = 6
	InvalidRedirect = 7
	NetFail = 8
	Aborted = 9
	SslConnectFail = 10
	SslVerificationFail = 11
	Unknown = 12
	pass

class HttpRequestType(Enum):
	Default = 0
	MarketplaceService = 2
	Players = 7
	Chat = 15
	Avatar = 16
	Analytics = 23
	Localization = 25
	pass

class HumanoidCollisionType(Enum):
	OuterBox = 0
	InnerBox = 1
	pass

class HumanoidDisplayDistanceType(Enum):
	Viewer = 0
	Subject = 1
	NONE = 2
	pass

class HumanoidHealthDisplayType(Enum):
	DisplayWhenDamaged = 0
	AlwaysOn = 1
	AlwaysOff = 2
	pass

class HumanoidOnlySetCollisionsOnStateChange(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class HumanoidRigType(Enum):
	R6 = 0
	R15 = 1
	pass

class HumanoidStateMachineMode(Enum):
	Default = 0
	Legacy = 1
	NoStateMachine = 2
	LuaStateMachine = 3
	pass

class HumanoidStateType(Enum):
	FallingDown = 0
	Running = 8
	RunningNoPhysics = 10
	Climbing = 12
	StrafingNoPhysics = 11
	Ragdoll = 1
	GettingUp = 2
	Jumping = 3
	Landed = 7
	Flying = 6
	Freefall = 5
	Seated = 13
	PlatformStanding = 14
	Dead = 15
	Swimming = 4
	Physics = 16
	NONE = 18
	pass

class IKCollisionsMode(Enum):
	NoCollisions = 0
	OtherMechanismsAnchored = 1
	IncludeContactedMechanisms = 2
	pass

class IKControlType(Enum):
	Transform = 0
	Position = 1
	Rotation = 2
	LookAt = 3
	pass

class IXPLoadingStatus(Enum):
	NONE = 0
	Pending = 1
	Initialized = 2
	ErrorTimedOut = 6
	ErrorConnection = 4
	ErrorJsonParse = 5
	ErrorInvalidUser = 3
	pass

class InOut(Enum):
	Edge = 0
	Inset = 1
	Center = 2
	pass

class InfoType(Enum):
	Asset = 0
	Product = 1
	GamePass = 2
	Subscription = 3
	Bundle = 4
	pass

class InitialDockState(Enum):
	Top = 0
	Bottom = 1
	Left = 2
	Right = 3
	Float = 4
	pass

class InputType(Enum):
	NoInput = 0
	Constant = 12
	Sin = 13
	pass

class InterpolationThrottlingMode(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class JointCreationMode(Enum):
	All = 0
	Surface = 1
	NONE = 2
	pass

class KeyCode(Enum):
	Unknown = 0
	Backspace = 8
	Tab = 9
	Clear = 12
	Return = 13
	Pause = 19
	Escape = 27
	Space = 32
	QuotedDouble = 34
	Hash = 35
	Dollar = 36
	Percent = 37
	Ampersand = 38
	Quote = 39
	LeftParenthesis = 40
	RightParenthesis = 41
	Asterisk = 42
	Plus = 43
	Comma = 44
	Minus = 45
	Period = 46
	Slash = 47
	Zero = 48
	One = 49
	Two = 50
	Three = 51
	Four = 52
	Five = 53
	Six = 54
	Seven = 55
	Eight = 56
	Nine = 57
	Colon = 58
	Semicolon = 59
	LessThan = 60
	Equals = 61
	GreaterThan = 62
	Question = 63
	At = 64
	LeftBracket = 91
	BackSlash = 92
	RightBracket = 93
	Caret = 94
	Underscore = 95
	Backquote = 96
	A = 97
	B = 98
	C = 99
	D = 100
	E = 101
	F = 102
	G = 103
	H = 104
	I = 105
	J = 106
	K = 107
	L = 108
	M = 109
	N = 110
	O = 111
	P = 112
	Q = 113
	R = 114
	S = 115
	T = 116
	U = 117
	V = 118
	W = 119
	X = 120
	Y = 121
	Z = 122
	LeftCurly = 123
	Pipe = 124
	RightCurly = 125
	Tilde = 126
	Delete = 127
	KeypadZero = 256
	KeypadOne = 257
	KeypadTwo = 258
	KeypadThree = 259
	KeypadFour = 260
	KeypadFive = 261
	KeypadSix = 262
	KeypadSeven = 263
	KeypadEight = 264
	KeypadNine = 265
	KeypadPeriod = 266
	KeypadDivide = 267
	KeypadMultiply = 268
	KeypadMinus = 269
	KeypadPlus = 270
	KeypadEnter = 271
	KeypadEquals = 272
	Up = 273
	Down = 274
	Right = 275
	Left = 276
	Insert = 277
	Home = 278
	End = 279
	PageUp = 280
	PageDown = 281
	LeftShift = 304
	RightShift = 303
	LeftMeta = 310
	RightMeta = 309
	LeftAlt = 308
	RightAlt = 307
	LeftControl = 306
	RightControl = 305
	CapsLock = 301
	NumLock = 300
	ScrollLock = 302
	LeftSuper = 311
	RightSuper = 312
	Mode = 313
	Compose = 314
	Help = 315
	Print = 316
	SysReq = 317
	Break = 318
	Menu = 319
	Power = 320
	Euro = 321
	Undo = 322
	F1 = 282
	F2 = 283
	F3 = 284
	F4 = 285
	F5 = 286
	F6 = 287
	F7 = 288
	F8 = 289
	F9 = 290
	F10 = 291
	F11 = 292
	F12 = 293
	F13 = 294
	F14 = 295
	F15 = 296
	World0 = 160
	World1 = 161
	World2 = 162
	World3 = 163
	World4 = 164
	World5 = 165
	World6 = 166
	World7 = 167
	World8 = 168
	World9 = 169
	World10 = 170
	World11 = 171
	World12 = 172
	World13 = 173
	World14 = 174
	World15 = 175
	World16 = 176
	World17 = 177
	World18 = 178
	World19 = 179
	World20 = 180
	World21 = 181
	World22 = 182
	World23 = 183
	World24 = 184
	World25 = 185
	World26 = 186
	World27 = 187
	World28 = 188
	World29 = 189
	World30 = 190
	World31 = 191
	World32 = 192
	World33 = 193
	World34 = 194
	World35 = 195
	World36 = 196
	World37 = 197
	World38 = 198
	World39 = 199
	World40 = 200
	World41 = 201
	World42 = 202
	World43 = 203
	World44 = 204
	World45 = 205
	World46 = 206
	World47 = 207
	World48 = 208
	World49 = 209
	World50 = 210
	World51 = 211
	World52 = 212
	World53 = 213
	World54 = 214
	World55 = 215
	World56 = 216
	World57 = 217
	World58 = 218
	World59 = 219
	World60 = 220
	World61 = 221
	World62 = 222
	World63 = 223
	World64 = 224
	World65 = 225
	World66 = 226
	World67 = 227
	World68 = 228
	World69 = 229
	World70 = 230
	World71 = 231
	World72 = 232
	World73 = 233
	World74 = 234
	World75 = 235
	World76 = 236
	World77 = 237
	World78 = 238
	World79 = 239
	World80 = 240
	World81 = 241
	World82 = 242
	World83 = 243
	World84 = 244
	World85 = 245
	World86 = 246
	World87 = 247
	World88 = 248
	World89 = 249
	World90 = 250
	World91 = 251
	World92 = 252
	World93 = 253
	World94 = 254
	World95 = 255
	ButtonX = 1000
	ButtonY = 1001
	ButtonA = 1002
	ButtonB = 1003
	ButtonR1 = 1004
	ButtonL1 = 1005
	ButtonR2 = 1006
	ButtonL2 = 1007
	ButtonR3 = 1008
	ButtonL3 = 1009
	ButtonStart = 1010
	ButtonSelect = 1011
	DPadLeft = 1012
	DPadRight = 1013
	DPadUp = 1014
	DPadDown = 1015
	Thumbstick1 = 1016
	Thumbstick2 = 1017
	pass

class KeyInterpolationMode(Enum):
	Constant = 0
	Linear = 1
	Cubic = 2
	pass

class KeywordFilterType(Enum):
	Include = 0
	Exclude = 1
	pass

class Language(Enum):
	Default = 0
	pass

class LeftRight(Enum):
	Left = 0
	Center = 1
	Right = 2
	pass

class LevelOfDetailSetting(Enum):
	High = 2
	Medium = 1
	Low = 0
	pass

class Limb(Enum):
	Head = 0
	Torso = 1
	LeftArm = 2
	RightArm = 3
	LeftLeg = 4
	RightLeg = 5
	Unknown = 6
	pass

class LineJoinMode(Enum):
	Round = 0
	Bevel = 1
	Miter = 2
	pass

class ListDisplayMode(Enum):
	Horizontal = 0
	Vertical = 1
	pass

class ListenerType(Enum):
	Camera = 0
	CFrame = 1
	ObjectPosition = 2
	ObjectCFrame = 3
	pass

class LoadCharacterLayeredClothing(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class LoadDynamicHeads(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class MarkupKind(Enum):
	PlainText = 0
	Markdown = 1
	pass

class Material(Enum):
	Plastic = 256
	Wood = 512
	Slate = 800
	Concrete = 816
	CorrodedMetal = 1040
	DiamondPlate = 1056
	Foil = 1072
	Grass = 1280
	Ice = 1536
	Marble = 784
	Granite = 832
	Brick = 848
	Pebble = 864
	Sand = 1296
	Fabric = 1312
	SmoothPlastic = 272
	Metal = 1088
	WoodPlanks = 528
	Cobblestone = 880
	Air = 1792
	Water = 2048
	Rock = 896
	Glacier = 1552
	Snow = 1328
	Sandstone = 912
	Mud = 1344
	Basalt = 788
	Ground = 1360
	CrackedLava = 804
	Neon = 288
	Glass = 1568
	Asphalt = 1376
	LeafyGrass = 1284
	Salt = 1392
	Limestone = 820
	Pavement = 836
	ForceField = 1584
	pass

class MaterialPattern(Enum):
	Regular = 0
	Organic = 1
	pass

class MembershipType(Enum):
	NONE = 0
	BuildersClub = 1
	TurboBuildersClub = 2
	OutrageousBuildersClub = 3
	Premium = 4
	pass

class MeshPartDetailLevel(Enum):
	DistanceBased = 0
	Level00 = 1
	Level01 = 2
	Level02 = 3
	Level03 = 4
	Level04 = 5
	pass

class MeshPartHeadsAndAccessories(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class MeshScaleUnit(Enum):
	Stud = 0
	Meter = 1
	CM = 2
	MM = 3
	Foot = 4
	Inch = 5
	pass

class MeshType(Enum):
	Head = 0
	Torso = 1
	Wedge = 2
	Prism = 7
	Pyramid = 8
	ParallelRamp = 9
	RightAngleRamp = 10
	CornerWedge = 11
	Brick = 6
	Sphere = 3
	Cylinder = 4
	FileMesh = 5
	pass

class MessageType(Enum):
	MessageOutput = 0
	MessageInfo = 1
	MessageWarning = 2
	MessageError = 3
	pass

class ModelLevelOfDetail(Enum):
	Automatic = 0
	StreamingMesh = 1
	Disabled = 2
	pass

class ModelStreamingMode(Enum):
	Default = 0
	Atomic = 1
	pass

class ModifierKey(Enum):
	Alt = 2
	Ctrl = 1
	Meta = 3
	Shift = 0
	pass

class MouseBehavior(Enum):
	Default = 0
	LockCenter = 1
	LockCurrentPosition = 2
	pass

class MoveState(Enum):
	Stopped = 0
	Coasting = 1
	Pushing = 2
	Stopping = 3
	AirFree = 4
	pass

class NameOcclusion(Enum):
	OccludeAll = 2
	EnemyOcclusion = 1
	NoOcclusion = 0
	pass

class NetworkOwnership(Enum):
	Automatic = 0
	Manual = 1
	OnContact = 2
	pass

class NewAnimationRuntimeSetting(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class NormalId(Enum):
	Top = 1
	Bottom = 4
	Back = 2
	Front = 5
	Right = 0
	Left = 3
	pass

class OrientationAlignmentMode(Enum):
	OneAttachment = 0
	TwoAttachment = 1
	pass

class OutfitSource(Enum):
	All = 1
	Created = 2
	Purchased = 3
	pass

class OutfitType(Enum):
	All = 1
	Avatar = 2
	DynamicHead = 3
	pass

class OutputLayoutMode(Enum):
	Horizontal = 0
	Vertical = 1
	pass

class OverrideMouseIconBehavior(Enum):
	NONE = 0
	ForceShow = 1
	ForceHide = 2
	pass

class PackagePermission(Enum):
	NONE = 0
	NoAccess = 1
	Revoked = 2
	UseView = 3
	Edit = 4
	Own = 5
	pass

class PartType(Enum):
	Ball = 0
	Block = 1
	Cylinder = 2
	pass

class ParticleEmitterShape(Enum):
	Box = 0
	Sphere = 1
	Cylinder = 2
	Disc = 3
	pass

class ParticleEmitterShapeInOut(Enum):
	Outward = 0
	Inward = 1
	InAndOut = 2
	pass

class ParticleEmitterShapeStyle(Enum):
	Volume = 0
	Surface = 1
	pass

class ParticleFlipbookLayout(Enum):
	NONE = 0
	Grid2x2 = 1
	Grid4x4 = 2
	Grid8x8 = 3
	pass

class ParticleFlipbookMode(Enum):
	Loop = 0
	OneShot = 1
	PingPong = 2
	Random = 3
	pass

class ParticleFlipbookTextureCompatible(Enum):
	NotCompatible = 0
	Compatible = 1
	Unknown = 2
	pass

class ParticleOrientation(Enum):
	FacingCamera = 0
	FacingCameraWorldUp = 1
	VelocityParallel = 2
	VelocityPerpendicular = 3
	pass

class PathStatus(Enum):
	Success = 0
	ClosestNoPath = 1
	ClosestOutOfRange = 2
	FailStartNotEmpty = 3
	FailFinishNotEmpty = 4
	NoPath = 5
	pass

class PathWaypointAction(Enum):
	Walk = 0
	Jump = 1
	Custom = 2
	pass

class PermissionLevelShown(Enum):
	Game = 0
	RobloxGame = 1
	RobloxScript = 2
	Studio = 3
	Roblox = 4
	pass

class PhysicsSimulationRate(Enum):
	Fixed240Hz = 0
	Fixed120Hz = 1
	Fixed60Hz = 2
	pass

class PhysicsSteppingMethod(Enum):
	Default = 0
	Fixed = 1
	Adaptive = 2
	pass

class PLATFORM(Enum):
	Windows = 0
	OSX = 1
	IOS = 2
	Android = 3
	XBoxOne = 4
	PS4 = 5
	PS3 = 6
	XBox360 = 7
	WiiU = 8
	NX = 9
	Ouya = 10
	AndroidTV = 11
	Chromecast = 12
	Linux = 13
	SteamOS = 14
	WebOS = 15
	DOS = 16
	BeOS = 17
	UWP = 18
	NONE = 19
	pass

class PlaybackState(Enum):
	Begin = 0
	Delayed = 1
	Playing = 2
	Paused = 3
	Completed = 4
	Cancelled = 5
	pass

class PlayerActions(Enum):
	CharacterForward = 0
	CharacterBackward = 1
	CharacterLeft = 2
	CharacterRight = 3
	CharacterJump = 4
	pass

class PlayerChatType(Enum):
	All = 0
	Team = 1
	Whisper = 2
	pass

class PoseEasingDirection(Enum):
	Out = 1
	InOut = 2
	In = 0
	pass

class PoseEasingStyle(Enum):
	Linear = 0
	Constant = 1
	Elastic = 2
	Cubic = 3
	Bounce = 4
	pass

class PositionAlignmentMode(Enum):
	OneAttachment = 0
	TwoAttachment = 1
	pass

class PrivilegeType(Enum):
	Owner = 255
	Admin = 240
	Member = 128
	Visitor = 10
	Banned = 0
	pass

class ProductLocationRestriction(Enum):
	AvatarShop = 0
	AllowedGames = 1
	AllGames = 2
	pass

class ProductPurchaseDecision(Enum):
	NotProcessedYet = 0
	PurchaseGranted = 1
	pass

class PropertyStatus(Enum):
	Ok = 0
	Warning = 1
	Error = 2
	pass

class ProximityPromptExclusivity(Enum):
	OnePerButton = 0
	OneGlobally = 1
	AlwaysShow = 2
	pass

class ProximityPromptInputType(Enum):
	Keyboard = 0
	Gamepad = 1
	Touch = 2
	pass

class ProximityPromptStyle(Enum):
	Default = 0
	Custom = 1
	pass

class QualityLevel(Enum):
	Automatic = 0
	Level01 = 1
	Level02 = 2
	Level03 = 3
	Level04 = 4
	Level05 = 5
	Level06 = 6
	Level07 = 7
	Level08 = 8
	Level09 = 9
	Level10 = 10
	Level11 = 11
	Level12 = 12
	Level13 = 13
	Level14 = 14
	Level15 = 15
	Level16 = 16
	Level17 = 17
	Level18 = 18
	Level19 = 19
	Level20 = 20
	Level21 = 21
	pass

class R15CollisionType(Enum):
	OuterBox = 0
	InnerBox = 1
	pass

class RaycastFilterType(Enum):
	Blacklist = 0
	Whitelist = 1
	pass

class RenderFidelity(Enum):
	Automatic = 0
	Precise = 1
	Performance = 2
	pass

class RenderPriority(Enum):
	First = 0
	Input = 100
	Camera = 200
	Character = 300
	Last = 2000
	pass

class RenderingTestComparisonMethod(Enum):
	psnr = 0
	diff = 1
	pass

class ReplicateInstanceDestroySetting(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class ResamplerMode(Enum):
	Default = 0
	Pixelated = 1
	pass

class ReservedHighlightId(Enum):
	Standard = 0
	Selection = 32
	Hover = 64
	Active = 128
	pass

class ReturnKeyType(Enum):
	Default = 0
	Done = 1
	Go = 2
	Next = 3
	Search = 4
	Send = 5
	pass

class ReverbType(Enum):
	NoReverb = 0
	GenericReverb = 1
	PaddedCell = 2
	Room = 3
	Bathroom = 4
	LivingRoom = 5
	StoneRoom = 6
	Auditorium = 7
	ConcertHall = 8
	Cave = 9
	Arena = 10
	Hangar = 11
	CarpettedHallway = 12
	Hallway = 13
	StoneCorridor = 14
	Alley = 15
	Forest = 16
	City = 17
	Mountains = 18
	Quarry = 19
	Plain = 20
	ParkingLot = 21
	SewerPipe = 22
	UnderWater = 23
	pass

class RibbonTool(Enum):
	Select = 0
	Scale = 1
	Rotate = 2
	Move = 3
	Transform = 4
	ColorPicker = 5
	MaterialPicker = 6
	Group = 7
	Ungroup = 8
	NONE = 9
	pass

class RigType(Enum):
	R15 = 0
	Rthro = 1
	RthroNarrow = 2
	Custom = 3
	NONE = 4
	pass

class RollOffMode(Enum):
	Inverse = 0
	Linear = 1
	InverseTapered = 3
	LinearSquare = 2
	pass

class RotationOrder(Enum):
	XYZ = 0
	XZY = 1
	YZX = 2
	YXZ = 3
	ZXY = 4
	ZYX = 5
	pass

class RotationType(Enum):
	MovementRelative = 0
	CameraRelative = 1
	pass

class RunContext(Enum):
	Legacy = 0
	Server = 1
	Client = 2
	Plugin = 3
	pass

class RuntimeUndoBehavior(Enum):
	Aggregate = 0
	Snapshot = 1
	Hybrid = 2
	pass

class SafeAreaCompatibility(Enum):
	NONE = 0
	FullscreenExtension = 1
	pass

class SaveFilter(Enum):
	SaveAll = 2
	SaveWorld = 0
	SaveGame = 1
	pass

class SavedQualitySetting(Enum):
	Automatic = 0
	QualityLevel1 = 1
	QualityLevel2 = 2
	QualityLevel3 = 3
	QualityLevel4 = 4
	QualityLevel5 = 5
	QualityLevel6 = 6
	QualityLevel7 = 7
	QualityLevel8 = 8
	QualityLevel9 = 9
	QualityLevel10 = 10
	pass

class ScaleType(Enum):
	Stretch = 0
	Slice = 1
	Tile = 2
	Fit = 3
	Crop = 4
	pass

class ScreenOrientation(Enum):
	LandscapeLeft = 0
	LandscapeRight = 1
	LandscapeSensor = 2
	Portrait = 3
	Sensor = 4
	pass

class ScrollBarInset(Enum):
	NONE = 0
	ScrollBar = 1
	Always = 2
	pass

class ScrollingDirection(Enum):
	X = 1
	Y = 2
	XY = 4
	pass

class SelectionBehavior(Enum):
	Escape = 0
	Stop = 1
	pass

class ServerAudioBehavior(Enum):
	Enabled = 0
	Muted = 1
	OnlineGame = 2
	pass

class SignalBehavior(Enum):
	Default = 0
	Immediate = 1
	Deferred = 2
	AncestryDeferred = 3
	pass

class SizeConstraint(Enum):
	RelativeXY = 0
	RelativeXX = 1
	RelativeYY = 2
	pass

class SortDirection(Enum):
	Ascending = 0
	Descending = 1
	pass

class SortOrder(Enum):
	LayoutOrder = 2
	Name = 0
	Custom = 1
	pass

class SpecialKey(Enum):
	Insert = 0
	Home = 1
	End = 2
	PageUp = 3
	PageDown = 4
	ChatHotkey = 5
	pass

class StartCorner(Enum):
	TopLeft = 0
	TopRight = 1
	BottomLeft = 2
	BottomRight = 3
	pass

class STATUS(Enum):
	Poison = 0
	Confusion = 1
	pass

class StreamOutBehavior(Enum):
	Default = 0
	LowMemory = 1
	Opportunistic = 2
	pass

class StreamingIntegrityMode(Enum):
	Default = 0
	Disabled = 1
	MinimumRadiusPause = 2
	PauseOutsideLoadedArea = 3
	pass

class StreamingPauseMode(Enum):
	Default = 0
	Disabled = 1
	ClientPhysicsPause = 2
	pass

class StudioCloseMode(Enum):
	NONE = 0
	CloseStudio = 1
	CloseDoc = 2
	pass

class StudioDataModelType(Enum):
	Edit = 0
	PlayClient = 1
	PlayServer = 2
	Standalone = 3
	NONE = 4
	pass

class StudioScriptEditorColorCategories(Enum):
	Default = 0
	Operator = 1
	Number = 2
	String = 3
	Comment = 4
	Keyword = 5
	Builtin = 6
	Method = 7
	Property = 8
	Nil = 9
	Bool = 10
	Function = 11
	Local = 12
	Self = 13
	LuauKeyword = 14
	FunctionName = 15
	TODO = 16
	Background = 17
	SelectionText = 18
	SelectionBackground = 19
	FindSelectionBackground = 20
	MatchingWordBackground = 21
	Warning = 22
	Error = 23
	Whitespace = 24
	ActiveLine = 25
	DebuggerCurrentLine = 26
	DebuggerErrorLine = 27
	Ruler = 28
	Bracket = 29
	MenuPrimaryText = 30
	MenuSecondaryText = 31
	MenuSelectedText = 32
	MenuBackground = 33
	MenuSelectedBackground = 34
	MenuScrollbarBackground = 35
	MenuScrollbarHandle = 36
	MenuBorder = 37
	DocViewCodeBackground = 38
	pass

class StudioScriptEditorColorPresets(Enum):
	RobloxDefault = 0
	Extra1 = 1
	Extra2 = 2
	Custom = 3
	pass

class StudioStyleGuideColor(Enum):
	MainBackground = 0
	Titlebar = 1
	Dropdown = 2
	Tooltip = 3
	Notification = 4
	ScrollBar = 5
	ScrollBarBackground = 6
	TabBar = 7
	Tab = 8
	FilterButtonDefault = 9
	FilterButtonHover = 10
	FilterButtonChecked = 11
	FilterButtonAccent = 12
	FilterButtonBorder = 13
	FilterButtonBorderAlt = 14
	RibbonTab = 15
	RibbonTabTopBar = 16
	Button = 17
	MainButton = 18
	RibbonButton = 19
	ViewPortBackground = 20
	InputFieldBackground = 21
	Item = 22
	TableItem = 23
	CategoryItem = 24
	GameSettingsTableItem = 25
	GameSettingsTooltip = 26
	EmulatorBar = 27
	EmulatorDropDown = 28
	ColorPickerFrame = 29
	CurrentMarker = 30
	Border = 31
	DropShadow = 32
	Shadow = 33
	Light = 34
	Dark = 35
	Mid = 36
	MainText = 37
	SubText = 38
	TitlebarText = 39
	BrightText = 40
	DimmedText = 41
	LinkText = 42
	WarningText = 43
	ErrorText = 44
	InfoText = 45
	SensitiveText = 46
	ScriptSideWidget = 47
	ScriptBackground = 48
	ScriptText = 49
	ScriptSelectionText = 50
	ScriptSelectionBackground = 51
	ScriptFindSelectionBackground = 52
	ScriptMatchingWordSelectionBackground = 53
	ScriptOperator = 54
	ScriptNumber = 55
	ScriptString = 56
	ScriptComment = 57
	ScriptKeyword = 58
	ScriptBuiltInFunction = 59
	ScriptWarning = 60
	ScriptError = 61
	ScriptWhitespace = 62
	ScriptRuler = 63
	DocViewCodeBackground = 64
	DebuggerCurrentLine = 65
	DebuggerErrorLine = 66
	ScriptEditorCurrentLine = 105
	DiffFilePathText = 67
	DiffTextHunkInfo = 68
	DiffTextNoChange = 69
	DiffTextAddition = 70
	DiffTextDeletion = 71
	DiffTextSeparatorBackground = 72
	DiffTextNoChangeBackground = 73
	DiffTextAdditionBackground = 74
	DiffTextDeletionBackground = 75
	DiffLineNum = 76
	DiffLineNumSeparatorBackground = 77
	DiffLineNumNoChangeBackground = 78
	DiffLineNumAdditionBackground = 79
	DiffLineNumDeletionBackground = 80
	DiffFilePathBackground = 81
	DiffFilePathBorder = 82
	ChatIncomingBgColor = 83
	ChatIncomingTextColor = 84
	ChatOutgoingBgColor = 85
	ChatOutgoingTextColor = 86
	ChatModeratedMessageColor = 87
	Separator = 88
	ButtonBorder = 89
	ButtonText = 90
	InputFieldBorder = 91
	CheckedFieldBackground = 92
	CheckedFieldBorder = 93
	CheckedFieldIndicator = 94
	HeaderSection = 95
	Midlight = 96
	StatusBar = 97
	DialogButton = 98
	DialogButtonText = 99
	DialogButtonBorder = 100
	DialogMainButton = 101
	DialogMainButtonText = 102
	InfoBarWarningBackground = 103
	InfoBarWarningText = 104
	ScriptMethod = 106
	ScriptProperty = 107
	ScriptNil = 108
	ScriptBool = 109
	ScriptFunction = 110
	ScriptLocal = 111
	ScriptSelf = 112
	ScriptLuauKeyword = 113
	ScriptFunctionName = 114
	ScriptTodo = 115
	ScriptBracket = 116
	AttributeCog = 117
	pass

class StudioStyleGuideModifier(Enum):
	Default = 0
	Selected = 1
	Pressed = 2
	Disabled = 3
	Hover = 4
	pass

class Style(Enum):
	AlternatingSupports = 0
	BridgeStyleSupports = 1
	NoSupports = 2
	pass

class SurfaceConstraint(Enum):
	NONE = 0
	Hinge = 1
	SteppingMotor = 2
	Motor = 3
	pass

class SurfaceGuiSizingMode(Enum):
	FixedSize = 0
	PixelsPerStud = 1
	pass

class SurfaceType(Enum):
	Smooth = 0
	Glue = 1
	Weld = 2
	Studs = 3
	Inlet = 4
	Universal = 5
	Hinge = 6
	Motor = 7
	SteppingMotor = 8
	SmoothNoOutlines = 10
	pass

class SwipeDirection(Enum):
	Right = 0
	Left = 1
	Up = 2
	Down = 3
	NONE = 4
	pass

class TableMajorAxis(Enum):
	RowMajor = 0
	ColumnMajor = 1
	pass

class Technology(Enum):
	Compatibility = 2
	Voxel = 1
	ShadowMap = 3
	Legacy = 0
	Future = 4
	pass

class TeleportMethod(Enum):
	TeleportToSpawnByName = 0
	TeleportToPlaceInstance = 1
	TeleportToPrivateServer = 2
	TeleportPartyAsync = 3
	TeleportUnknown = 4
	pass

class TeleportResult(Enum):
	Success = 0
	Failure = 1
	GameNotFound = 2
	GameEnded = 3
	GameFull = 4
	Unauthorized = 5
	Flooded = 6
	IsTeleporting = 7
	pass

class TeleportState(Enum):
	RequestedFromServer = 0
	Started = 1
	WaitingForServer = 2
	Failed = 3
	InProgress = 4
	pass

class TeleportType(Enum):
	ToPlace = 0
	ToInstance = 1
	ToReservedServer = 2
	pass

class TerrainAcquisitionMethod(Enum):
	NONE = 0
	Legacy = 1
	Template = 2
	Generate = 3
	Import = 4
	Convert = 5
	EditAddTool = 6
	EditSeaLevelTool = 7
	EditReplaceTool = 8
	RegionFillTool = 9
	RegionPasteTool = 10
	Other = 11
	pass

class TerrainFace(Enum):
	Top = 0
	Side = 1
	Bottom = 2
	pass

class TextChatMessageStatus(Enum):
	Unknown = 1
	Success = 2
	Sending = 3
	TextFilterFailed = 4
	Floodchecked = 5
	InvalidPrivacySettings = 6
	InvalidTextChannelPermissions = 7
	MessageTooLong = 8
	pass

class TextFilterContext(Enum):
	PublicChat = 1
	PrivateChat = 2
	pass

class TextInputType(Enum):
	Default = 0
	NoSuggestions = 1
	Number = 2
	Email = 3
	Phone = 4
	Password = 5
	PasswordShown = 6
	Username = 7
	OneTimePassword = 8
	pass

class TextTruncate(Enum):
	NONE = 0
	AtEnd = 1
	pass

class TextXAlignment(Enum):
	Left = 0
	Center = 2
	Right = 1
	pass

class TextYAlignment(Enum):
	Top = 0
	Center = 1
	Bottom = 2
	pass

class TextureMode(Enum):
	Stretch = 0
	Wrap = 1
	Static = 2
	pass

class TextureQueryType(Enum):
	NonHumanoid = 0
	NonHumanoidOrphaned = 1
	Humanoid = 2
	HumanoidOrphaned = 3
	pass

class ThreadPoolConfig(Enum):
	Auto = 0
	PerCore1 = 101
	PerCore2 = 102
	PerCore3 = 103
	PerCore4 = 104
	Threads1 = 1
	Threads2 = 2
	Threads3 = 3
	Threads4 = 4
	Threads8 = 8
	Threads16 = 16
	pass

class ThrottlingPriority(Enum):
	Extreme = 2
	ElevatedOnServer = 1
	Default = 0
	pass

class ThumbnailSize(Enum):
	Size48x48 = 0
	Size180x180 = 1
	Size420x420 = 2
	Size60x60 = 3
	Size100x100 = 4
	Size150x150 = 5
	Size352x352 = 6
	pass

class ThumbnailType(Enum):
	HeadShot = 0
	AvatarBust = 1
	AvatarThumbnail = 2
	pass

class TickCountSampleMethod(Enum):
	Fast = 0
	Benchmark = 1
	Precise = 2
	pass

class TopBottom(Enum):
	Top = 0
	Center = 1
	Bottom = 2
	pass

class TouchCameraMovementMode(Enum):
	Default = 0
	Follow = 2
	Classic = 1
	Orbital = 3
	pass

class TouchMovementMode(Enum):
	Default = 0
	Thumbstick = 1
	DPad = 2
	Thumbpad = 3
	ClickToMove = 4
	DynamicThumbstick = 5
	pass

class TrackerError(Enum):
	Ok = 0
	NoService = 1
	InitFailed = 2
	NoVideo = 3
	VideoError = 4
	VideoNoPermission = 5
	NoAudio = 6
	AudioError = 7
	AudioNoPermission = 8
	pass

class TrackerExtrapolationFlagMode(Enum):
	Auto = 3
	ForceDisabled = 0
	ExtrapolateFacsAndPose = 1
	ExtrapolateFacsOnly = 2
	pass

class TrackerLodFlagMode(Enum):
	Auto = 2
	ForceFalse = 0
	ForceTrue = 1
	pass

class TrackerLodValueMode(Enum):
	Auto = 2
	Force0 = 0
	Force1 = 1
	pass

class TrackerMode(Enum):
	NONE = 0
	Audio = 1
	Video = 2
	AudioVideo = 3
	pass

class TriStateBoolean(Enum):
	Unknown = 0
	TRUE = 1
	FALSE = 2
	pass

class TweenStatus(Enum):
	Canceled = 0
	Completed = 1
	pass

class UITheme(Enum):
	Light = 0
	Dark = 1
	pass

class UiMessageType(Enum):
	UiMessageError = 0
	UiMessageInfo = 1
	pass

class UnionsScaleNonuniformly(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class UsageContext(Enum):
	Default = 0
	Preview = 1
	pass

class UserCFrame(Enum):
	Head = 0
	LeftHand = 1
	RightHand = 2
	pass

class UserInputState(Enum):
	Begin = 0
	Change = 1
	End = 2
	Cancel = 3
	NONE = 4
	pass

class UserInputType(Enum):
	MouseButton1 = 0
	MouseButton2 = 1
	MouseButton3 = 2
	MouseWheel = 3
	MouseMovement = 4
	Touch = 7
	Keyboard = 8
	Focus = 9
	Accelerometer = 10
	Gyro = 11
	Gamepad1 = 12
	Gamepad2 = 13
	Gamepad3 = 14
	Gamepad4 = 15
	Gamepad5 = 16
	Gamepad6 = 17
	Gamepad7 = 18
	Gamepad8 = 19
	TextInput = 20
	InputMethod = 21
	NONE = 22
	pass

class VRTouchpad(Enum):
	Left = 0
	Right = 1
	pass

class VRTouchpadMode(Enum):
	Touch = 0
	VirtualThumbstick = 1
	ABXY = 2
	pass

class VelocityConstraintMode(Enum):
	Line = 0
	Plane = 1
	Vector = 2
	pass

class VerticalAlignment(Enum):
	Center = 0
	Top = 1
	Bottom = 2
	pass

class VerticalScrollBarPosition(Enum):
	Left = 1
	Right = 0
	pass

class VibrationMotor(Enum):
	Large = 0
	Small = 1
	LeftTrigger = 2
	RightTrigger = 3
	LeftHand = 4
	RightHand = 5
	pass

class VirtualCursorMode(Enum):
	Default = 0
	Disabled = 1
	Enabled = 2
	pass

class VirtualInputMode(Enum):
	Recording = 1
	Playing = 2
	NONE = 0
	pass

class VoiceChatState(Enum):
	Idle = 0
	Joining = 1
	JoiningRetry = 2
	Joined = 3
	Leaving = 4
	Ended = 5
	Failed = 6
	pass

class VolumetricAudio(Enum):
	Disabled = 0
	Automatic = 1
	Enabled = 2
	pass

class WaterDirection(Enum):
	NegX = 0
	X = 1
	NegY = 2
	Y = 3
	NegZ = 4
	Z = 5
	pass

class WaterForce(Enum):
	NONE = 0
	Small = 1
	Medium = 2
	Strong = 3
	Max = 4
	pass

class WrapLayerAutoSkin(Enum):
	Disabled = 0
	EnabledPreserve = 1
	EnabledOverride = 2
	pass

class WrapLayerDebugMode(Enum):
	NONE = 0
	BoundCage = 1
	LayerCage = 2
	BoundCageAndLinks = 3
	Reference = 4
	Rbf = 5
	OuterCage = 6
	ReferenceMeshAfterMorph = 7
	HSROuterDetail = 8
	HSROuter = 9
	HSRInner = 10
	HSRInnerReverse = 11
	LayerCageFittedToBase = 12
	LayerCageFittedToPrev = 13
	pass

class WrapTargetDebugMode(Enum):
	NONE = 0
	TargetCageOriginal = 1
	TargetCageCompressed = 2
	TargetCageInterface = 3
	TargetLayerCageOriginal = 4
	TargetLayerCageCompressed = 5
	TargetLayerInterface = 6
	Rbf = 7
	OuterCageDetail = 8
	pass

class ZIndexBehavior(Enum):
	Global = 0
	Sibling = 1
	pass

class Instance:
	Archivable: bool
	ClassName: str
	DataCost: int
	Name: str
	Parent: 'Instance'
	RobloxLocked: bool
	SourceAssetId: int
	archivable: bool
	className: str
	@singledispatchmethod
	@classmethod
	def new(cls, className: str, parent: Self | None = None) -> None:
		if isinstance(className, Literal["Accoutrement"]):
			a = Accoutrement()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Accessory"]):
			a = Accessory()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Hat"]):
			a = Hat()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AdPortal"]):
			a = AdPortal()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AdService"]):
			a = AdService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AdvancedDragger"]):
			a = AdvancedDragger()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnalyticsService"]):
			a = AnalyticsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Animation"]):
			a = Animation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationClip"]):
			a = AnimationClip()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CurveAnimation"]):
			a = CurveAnimation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["KeyframeSequence"]):
			a = KeyframeSequence()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationClipProvider"]):
			a = AnimationClipProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationController"]):
			a = AnimationController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationFromVideoCreatorService"]):
			a = AnimationFromVideoCreatorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationFromVideoCreatorStudioService"]):
			a = AnimationFromVideoCreatorStudioService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationRigData"]):
			a = AnimationRigData()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationStreamTrack"]):
			a = AnimationStreamTrack()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationTrack"]):
			a = AnimationTrack()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Animator"]):
			a = Animator()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AppUpdateService"]):
			a = AppUpdateService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetCounterService"]):
			a = AssetCounterService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetDeliveryProxy"]):
			a = AssetDeliveryProxy()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetImportService"]):
			a = AssetImportService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetImportSession"]):
			a = AssetImportSession()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetManagerService"]):
			a = AssetManagerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetPatchSettings"]):
			a = AssetPatchSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetService"]):
			a = AssetService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Atmosphere"]):
			a = Atmosphere()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Attachment"]):
			a = Attachment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Bone"]):
			a = Bone()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AvatarEditorService"]):
			a = AvatarEditorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AvatarImportService"]):
			a = AvatarImportService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Backpack"]):
			a = Backpack()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BackpackItem"]):
			a = BackpackItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HopperBin"]):
			a = HopperBin()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Tool"]):
			a = Tool()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Flag"]):
			a = Flag()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BadgeService"]):
			a = BadgeService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BasePlayerGui"]):
			a = BasePlayerGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CoreGui"]):
			a = CoreGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PlayerGui"]):
			a = PlayerGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterGui"]):
			a = StarterGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BaseWrap"]):
			a = BaseWrap()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WrapLayer"]):
			a = WrapLayer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WrapTarget"]):
			a = WrapTarget()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Beam"]):
			a = Beam()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BindableEvent"]):
			a = BindableEvent()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BindableFunction"]):
			a = BindableFunction()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyMover"]):
			a = BodyMover()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyAngularVelocity"]):
			a = BodyAngularVelocity()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyForce"]):
			a = BodyForce()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyGyro"]):
			a = BodyGyro()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyPosition"]):
			a = BodyPosition()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyThrust"]):
			a = BodyThrust()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyVelocity"]):
			a = BodyVelocity()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RocketPropulsion"]):
			a = RocketPropulsion()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Breakpoint"]):
			a = Breakpoint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BrowserService"]):
			a = BrowserService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BulkImportService"]):
			a = BulkImportService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CacheableContentProvider"]):
			a = CacheableContentProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HSRDataContentProvider"]):
			a = HSRDataContentProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MeshContentProvider"]):
			a = MeshContentProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SolidModelContentProvider"]):
			a = SolidModelContentProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CalloutService"]):
			a = CalloutService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Camera"]):
			a = Camera()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ChangeHistoryService"]):
			a = ChangeHistoryService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CharacterAppearance"]):
			a = CharacterAppearance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BodyColors"]):
			a = BodyColors()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CharacterMesh"]):
			a = CharacterMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Clothing"]):
			a = Clothing()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Pants"]):
			a = Pants()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Shirt"]):
			a = Shirt()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ShirtGraphic"]):
			a = ShirtGraphic()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Skin"]):
			a = Skin()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Chat"]):
			a = Chat()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ClickDetector"]):
			a = ClickDetector()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Clouds"]):
			a = Clouds()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ClusterPacketCache"]):
			a = ClusterPacketCache()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CollectionService"]):
			a = CollectionService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CommandInstance"]):
			a = CommandInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CommandService"]):
			a = CommandService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Configuration"]):
			a = Configuration()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ConfigureServerService"]):
			a = ConfigureServerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Constraint"]):
			a = Constraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AlignOrientation"]):
			a = AlignOrientation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AlignPosition"]):
			a = AlignPosition()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AngularVelocity"]):
			a = AngularVelocity()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnimationConstraint"]):
			a = AnimationConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BallSocketConstraint"]):
			a = BallSocketConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HingeConstraint"]):
			a = HingeConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LineForce"]):
			a = LineForce()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LinearVelocity"]):
			a = LinearVelocity()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PlaneConstraint"]):
			a = PlaneConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Plane"]):
			a = Plane()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RigidConstraint"]):
			a = RigidConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RodConstraint"]):
			a = RodConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RopeConstraint"]):
			a = RopeConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SlidingBallConstraint"]):
			a = SlidingBallConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CylindricalConstraint"]):
			a = CylindricalConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PrismaticConstraint"]):
			a = PrismaticConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SpringConstraint"]):
			a = SpringConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Torque"]):
			a = Torque()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TorsionSpringConstraint"]):
			a = TorsionSpringConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UniversalConstraint"]):
			a = UniversalConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VectorForce"]):
			a = VectorForce()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ContentProvider"]):
			a = ContentProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ContextActionService"]):
			a = ContextActionService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Controller"]):
			a = Controller()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HumanoidController"]):
			a = HumanoidController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SkateboardController"]):
			a = SkateboardController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VehicleController"]):
			a = VehicleController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ControllerBase"]):
			a = ControllerBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AirController"]):
			a = AirController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ClimbController"]):
			a = ClimbController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GroundController"]):
			a = GroundController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SwimController"]):
			a = SwimController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ControllerManager"]):
			a = ControllerManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ControllerService"]):
			a = ControllerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CookiesService"]):
			a = CookiesService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CorePackages"]):
			a = CorePackages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CoreScriptSyncService"]):
			a = CoreScriptSyncService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CrossDMScriptChangeListener"]):
			a = CrossDMScriptChangeListener()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CustomEvent"]):
			a = CustomEvent()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CustomEventReceiver"]):
			a = CustomEventReceiver()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataModelMesh"]):
			a = DataModelMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BevelMesh"]):
			a = BevelMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BlockMesh"]):
			a = BlockMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CylinderMesh"]):
			a = CylinderMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FileMesh"]):
			a = FileMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SpecialMesh"]):
			a = SpecialMesh()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataModelPatchService"]):
			a = DataModelPatchService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataModelSession"]):
			a = DataModelSession()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreIncrementOptions"]):
			a = DataStoreIncrementOptions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreInfo"]):
			a = DataStoreInfo()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreKey"]):
			a = DataStoreKey()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreKeyInfo"]):
			a = DataStoreKeyInfo()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreObjectVersionInfo"]):
			a = DataStoreObjectVersionInfo()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreOptions"]):
			a = DataStoreOptions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreService"]):
			a = DataStoreService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreSetOptions"]):
			a = DataStoreSetOptions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Debris"]):
			a = Debris()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebugSettings"]):
			a = DebugSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggablePluginWatcher"]):
			a = DebuggablePluginWatcher()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerBreakpoint"]):
			a = DebuggerBreakpoint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerConnection"]):
			a = DebuggerConnection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LocalDebuggerConnection"]):
			a = LocalDebuggerConnection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerConnectionManager"]):
			a = DebuggerConnectionManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerLuaResponse"]):
			a = DebuggerLuaResponse()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerManager"]):
			a = DebuggerManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerUIService"]):
			a = DebuggerUIService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerVariable"]):
			a = DebuggerVariable()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DebuggerWatch"]):
			a = DebuggerWatch()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DeviceIdService"]):
			a = DeviceIdService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Dialog"]):
			a = Dialog()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DialogChoice"]):
			a = DialogChoice()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DraftsService"]):
			a = DraftsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Dragger"]):
			a = Dragger()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DraggerService"]):
			a = DraggerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["EulerRotationCurve"]):
			a = EulerRotationCurve()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["EventIngestService"]):
			a = EventIngestService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ExperienceInviteOptions"]):
			a = ExperienceInviteOptions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Explosion"]):
			a = Explosion()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FaceAnimatorService"]):
			a = FaceAnimatorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FaceControls"]):
			a = FaceControls()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FaceInstance"]):
			a = FaceInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Decal"]):
			a = Decal()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Texture"]):
			a = Texture()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FacialAnimationRecordingService"]):
			a = FacialAnimationRecordingService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FacialAnimationStreamingService"]):
			a = FacialAnimationStreamingService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FacialAnimationStreamingServiceV2"]):
			a = FacialAnimationStreamingServiceV2()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Feature"]):
			a = Feature()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Hole"]):
			a = Hole()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MotorFeature"]):
			a = MotorFeature()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["File"]):
			a = File()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Fire"]):
			a = Fire()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FlagStandService"]):
			a = FlagStandService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FloatCurve"]):
			a = FloatCurve()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FlyweightService"]):
			a = FlyweightService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CSGDictionaryService"]):
			a = CSGDictionaryService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NonReplicatedCSGDictionaryService"]):
			a = NonReplicatedCSGDictionaryService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Folder"]):
			a = Folder()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ForceField"]):
			a = ForceField()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FriendService"]):
			a = FriendService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FunctionalTest"]):
			a = FunctionalTest()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GamePassService"]):
			a = GamePassService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GameSettings"]):
			a = GameSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GamepadService"]):
			a = GamepadService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Geometry"]):
			a = Geometry()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GetTextBoundsParams"]):
			a = GetTextBoundsParams()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GlobalDataStore"]):
			a = GlobalDataStore()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStore"]):
			a = DataStore()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["OrderedDataStore"]):
			a = OrderedDataStore()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GoogleAnalyticsConfiguration"]):
			a = GoogleAnalyticsConfiguration()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GroupService"]):
			a = GroupService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiBase"]):
			a = GuiBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiBase2d"]):
			a = GuiBase2d()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiObject"]):
			a = GuiObject()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CanvasGroup"]):
			a = CanvasGroup()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Frame"]):
			a = Frame()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiButton"]):
			a = GuiButton()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImageButton"]):
			a = ImageButton()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextButton"]):
			a = TextButton()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiLabel"]):
			a = GuiLabel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImageLabel"]):
			a = ImageLabel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextLabel"]):
			a = TextLabel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScrollingFrame"]):
			a = ScrollingFrame()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextBox"]):
			a = TextBox()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VideoFrame"]):
			a = VideoFrame()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ViewportFrame"]):
			a = ViewportFrame()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LayerCollector"]):
			a = LayerCollector()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BillboardGui"]):
			a = BillboardGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginGui"]):
			a = PluginGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DockWidgetPluginGui"]):
			a = DockWidgetPluginGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["QWidgetPluginGui"]):
			a = QWidgetPluginGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScreenGui"]):
			a = ScreenGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiMain"]):
			a = GuiMain()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SurfaceGuiBase"]):
			a = SurfaceGuiBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AdGui"]):
			a = AdGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SurfaceGui"]):
			a = SurfaceGui()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiBase3d"]):
			a = GuiBase3d()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FloorWire"]):
			a = FloorWire()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["InstanceAdornment"]):
			a = InstanceAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SelectionBox"]):
			a = SelectionBox()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PVAdornment"]):
			a = PVAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HandleAdornment"]):
			a = HandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BoxHandleAdornment"]):
			a = BoxHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ConeHandleAdornment"]):
			a = ConeHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CylinderHandleAdornment"]):
			a = CylinderHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImageHandleAdornment"]):
			a = ImageHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LineHandleAdornment"]):
			a = LineHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SphereHandleAdornment"]):
			a = SphereHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WireframeHandleAdornment"]):
			a = WireframeHandleAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ParabolaAdornment"]):
			a = ParabolaAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SelectionSphere"]):
			a = SelectionSphere()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PartAdornment"]):
			a = PartAdornment()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HandlesBase"]):
			a = HandlesBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ArcHandles"]):
			a = ArcHandles()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Handles"]):
			a = Handles()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SurfaceSelection"]):
			a = SurfaceSelection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SelectionLasso"]):
			a = SelectionLasso()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SelectionPartLasso"]):
			a = SelectionPartLasso()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SelectionPointLasso"]):
			a = SelectionPointLasso()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuiService"]):
			a = GuiService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GuidRegistryService"]):
			a = GuidRegistryService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HapticService"]):
			a = HapticService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HeightmapImporterService"]):
			a = HeightmapImporterService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HiddenSurfaceRemovalAsset"]):
			a = HiddenSurfaceRemovalAsset()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Highlight"]):
			a = Highlight()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Hopper"]):
			a = Hopper()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HttpRbxApiService"]):
			a = HttpRbxApiService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HttpRequest"]):
			a = HttpRequest()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HttpService"]):
			a = HttpService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Humanoid"]):
			a = Humanoid()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["HumanoidDescription"]):
			a = HumanoidDescription()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["IKControl"]):
			a = IKControl()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ILegacyStudioBridge"]):
			a = ILegacyStudioBridge()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LegacyStudioBridge"]):
			a = LegacyStudioBridge()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["IXPService"]):
			a = IXPService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterBaseSettings"]):
			a = ImporterBaseSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterAnimationSettings"]):
			a = ImporterAnimationSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterFacsSettings"]):
			a = ImporterFacsSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterGroupSettings"]):
			a = ImporterGroupSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterJointSettings"]):
			a = ImporterJointSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterMaterialSettings"]):
			a = ImporterMaterialSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterMeshSettings"]):
			a = ImporterMeshSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ImporterRootSettings"]):
			a = ImporterRootSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["IncrementalPatchBuilder"]):
			a = IncrementalPatchBuilder()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["InputObject"]):
			a = InputObject()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["InsertService"]):
			a = InsertService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["JointInstance"]):
			a = JointInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DynamicRotate"]):
			a = DynamicRotate()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RotateP"]):
			a = RotateP()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RotateV"]):
			a = RotateV()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Glue"]):
			a = Glue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ManualSurfaceJointInstance"]):
			a = ManualSurfaceJointInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ManualGlue"]):
			a = ManualGlue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ManualWeld"]):
			a = ManualWeld()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Motor"]):
			a = Motor()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Motor6D"]):
			a = Motor6D()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Rotate"]):
			a = Rotate()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Snap"]):
			a = Snap()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VelocityMotor"]):
			a = VelocityMotor()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Weld"]):
			a = Weld()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["JointsService"]):
			a = JointsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["KeyboardService"]):
			a = KeyboardService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Keyframe"]):
			a = Keyframe()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["KeyframeMarker"]):
			a = KeyframeMarker()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["KeyframeSequenceProvider"]):
			a = KeyframeSequenceProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LSPFileSyncService"]):
			a = LSPFileSyncService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LanguageService"]):
			a = LanguageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Light"]):
			a = Light()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PointLight"]):
			a = PointLight()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SpotLight"]):
			a = SpotLight()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SurfaceLight"]):
			a = SurfaceLight()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Lighting"]):
			a = Lighting()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LocalStorageService"]):
			a = LocalStorageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AppStorageService"]):
			a = AppStorageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UserStorageService"]):
			a = UserStorageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LocalizationService"]):
			a = LocalizationService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LocalizationTable"]):
			a = LocalizationTable()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CloudLocalizationTable"]):
			a = CloudLocalizationTable()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LodDataEntity"]):
			a = LodDataEntity()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LodDataService"]):
			a = LodDataService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LogService"]):
			a = LogService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LoginService"]):
			a = LoginService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LuaSettings"]):
			a = LuaSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LuaSourceContainer"]):
			a = LuaSourceContainer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BaseScript"]):
			a = BaseScript()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CoreScript"]):
			a = CoreScript()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Script"]):
			a = Script()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LocalScript"]):
			a = LocalScript()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ModuleScript"]):
			a = ModuleScript()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LuaWebService"]):
			a = LuaWebService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["LuauScriptAnalyzerService"]):
			a = LuauScriptAnalyzerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MarkerCurve"]):
			a = MarkerCurve()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MarketplaceService"]):
			a = MarketplaceService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MaterialService"]):
			a = MaterialService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MaterialVariant"]):
			a = MaterialVariant()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MemStorageConnection"]):
			a = MemStorageConnection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MemStorageService"]):
			a = MemStorageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MemoryStoreQueue"]):
			a = MemoryStoreQueue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MemoryStoreService"]):
			a = MemoryStoreService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MemoryStoreSortedMap"]):
			a = MemoryStoreSortedMap()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Message"]):
			a = Message()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Hint"]):
			a = Hint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MessageBusConnection"]):
			a = MessageBusConnection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MessageBusService"]):
			a = MessageBusService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MessagingService"]):
			a = MessagingService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MetaBreakpoint"]):
			a = MetaBreakpoint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MetaBreakpointContext"]):
			a = MetaBreakpointContext()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MetaBreakpointManager"]):
			a = MetaBreakpointManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Mouse"]):
			a = Mouse()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PlayerMouse"]):
			a = PlayerMouse()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginMouse"]):
			a = PluginMouse()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MouseService"]):
			a = MouseService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MultipleDocumentInterfaceInstance"]):
			a = MultipleDocumentInterfaceInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkMarker"]):
			a = NetworkMarker()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkPeer"]):
			a = NetworkPeer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkClient"]):
			a = NetworkClient()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkServer"]):
			a = NetworkServer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkReplicator"]):
			a = NetworkReplicator()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ClientReplicator"]):
			a = ClientReplicator()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ServerReplicator"]):
			a = ServerReplicator()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NetworkSettings"]):
			a = NetworkSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NoCollisionConstraint"]):
			a = NoCollisionConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NotificationService"]):
			a = NotificationService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PVInstance"]):
			a = PVInstance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BasePart"]):
			a = BasePart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CornerWedgePart"]):
			a = CornerWedgePart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FormFactorPart"]):
			a = FormFactorPart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Part"]):
			a = Part()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FlagStand"]):
			a = FlagStand()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Platform"]):
			a = Platform()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Seat"]):
			a = Seat()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SkateboardPlatform"]):
			a = SkateboardPlatform()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SpawnLocation"]):
			a = SpawnLocation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WedgePart"]):
			a = WedgePart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Terrain"]):
			a = Terrain()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TriangleMeshPart"]):
			a = TriangleMeshPart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["MeshPart"]):
			a = MeshPart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PartOperation"]):
			a = PartOperation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NegateOperation"]):
			a = NegateOperation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UnionOperation"]):
			a = UnionOperation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TrussPart"]):
			a = TrussPart()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VehicleSeat"]):
			a = VehicleSeat()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Model"]):
			a = Model()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Actor"]):
			a = Actor()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Status"]):
			a = Status()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WorldRoot"]):
			a = WorldRoot()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Workspace"]):
			a = Workspace()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WorldModel"]):
			a = WorldModel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PackageLink"]):
			a = PackageLink()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PackageService"]):
			a = PackageService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PackageUIService"]):
			a = PackageUIService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Pages"]):
			a = Pages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CatalogPages"]):
			a = CatalogPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreKeyPages"]):
			a = DataStoreKeyPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreListingPages"]):
			a = DataStoreListingPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStorePages"]):
			a = DataStorePages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataStoreVersionPages"]):
			a = DataStoreVersionPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FriendPages"]):
			a = FriendPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["InventoryPages"]):
			a = InventoryPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["EmotesPages"]):
			a = EmotesPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["OutfitPages"]):
			a = OutfitPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StandardPages"]):
			a = StandardPages()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PartOperationAsset"]):
			a = PartOperationAsset()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ParticleEmitter"]):
			a = ParticleEmitter()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Path"]):
			a = Path()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PathfindingLink"]):
			a = PathfindingLink()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PathfindingModifier"]):
			a = PathfindingModifier()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PathfindingService"]):
			a = PathfindingService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PausedState"]):
			a = PausedState()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PausedStateBreakpoint"]):
			a = PausedStateBreakpoint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PausedStateException"]):
			a = PausedStateException()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PermissionsService"]):
			a = PermissionsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PhysicsService"]):
			a = PhysicsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PhysicsSettings"]):
			a = PhysicsSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Player"]):
			a = Player()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PlayerEmulatorService"]):
			a = PlayerEmulatorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PlayerScripts"]):
			a = PlayerScripts()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Players"]):
			a = Players()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Plugin"]):
			a = Plugin()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginAction"]):
			a = PluginAction()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginDebugService"]):
			a = PluginDebugService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginDragEvent"]):
			a = PluginDragEvent()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginGuiService"]):
			a = PluginGuiService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginManagementService"]):
			a = PluginManagementService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginManager"]):
			a = PluginManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginManagerInterface"]):
			a = PluginManagerInterface()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginMenu"]):
			a = PluginMenu()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginPolicyService"]):
			a = PluginPolicyService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginToolbar"]):
			a = PluginToolbar()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PluginToolbarButton"]):
			a = PluginToolbarButton()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PointsService"]):
			a = PointsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PolicyService"]):
			a = PolicyService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PoseBase"]):
			a = PoseBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NumberPose"]):
			a = NumberPose()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Pose"]):
			a = Pose()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PostEffect"]):
			a = PostEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BloomEffect"]):
			a = BloomEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BlurEffect"]):
			a = BlurEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ColorCorrectionEffect"]):
			a = ColorCorrectionEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DepthOfFieldEffect"]):
			a = DepthOfFieldEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SunRaysEffect"]):
			a = SunRaysEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ProcessInstancePhysicsService"]):
			a = ProcessInstancePhysicsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ProximityPrompt"]):
			a = ProximityPrompt()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ProximityPromptService"]):
			a = ProximityPromptService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PublishService"]):
			a = PublishService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RbxAnalyticsService"]):
			a = RbxAnalyticsService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadata"]):
			a = ReflectionMetadata()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataCallbacks"]):
			a = ReflectionMetadataCallbacks()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataClasses"]):
			a = ReflectionMetadataClasses()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataEnums"]):
			a = ReflectionMetadataEnums()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataEvents"]):
			a = ReflectionMetadataEvents()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataFunctions"]):
			a = ReflectionMetadataFunctions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataItem"]):
			a = ReflectionMetadataItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataClass"]):
			a = ReflectionMetadataClass()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataEnum"]):
			a = ReflectionMetadataEnum()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataEnumItem"]):
			a = ReflectionMetadataEnumItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataMember"]):
			a = ReflectionMetadataMember()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataProperties"]):
			a = ReflectionMetadataProperties()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReflectionMetadataYieldFunctions"]):
			a = ReflectionMetadataYieldFunctions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RemoteDebuggerServer"]):
			a = RemoteDebuggerServer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RemoteEvent"]):
			a = RemoteEvent()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RemoteFunction"]):
			a = RemoteFunction()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RenderSettings"]):
			a = RenderSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RenderingTest"]):
			a = RenderingTest()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReplicatedFirst"]):
			a = ReplicatedFirst()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReplicatedStorage"]):
			a = ReplicatedStorage()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RobloxPluginGuiService"]):
			a = RobloxPluginGuiService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RobloxReplicatedStorage"]):
			a = RobloxReplicatedStorage()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RotationCurve"]):
			a = RotationCurve()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RtMessagingService"]):
			a = RtMessagingService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RunService"]):
			a = RunService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RuntimeScriptService"]):
			a = RuntimeScriptService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScreenshotHud"]):
			a = ScreenshotHud()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptBuilder"]):
			a = ScriptBuilder()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CoreScriptBuilder"]):
			a = CoreScriptBuilder()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptChangeService"]):
			a = ScriptChangeService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptCloneWatcher"]):
			a = ScriptCloneWatcher()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptCloneWatcherHelper"]):
			a = ScriptCloneWatcherHelper()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptContext"]):
			a = ScriptContext()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptDebugger"]):
			a = ScriptDebugger()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptDocument"]):
			a = ScriptDocument()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptEditorService"]):
			a = ScriptEditorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptRegistrationService"]):
			a = ScriptRegistrationService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ScriptService"]):
			a = ScriptService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Selection"]):
			a = Selection()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ServerScriptService"]):
			a = ServerScriptService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ServerStorage"]):
			a = ServerStorage()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ServiceProvider"]):
			a = ServiceProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DataModel"]):
			a = DataModel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GenericSettings"]):
			a = GenericSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AnalysticsSettings"]):
			a = AnalysticsSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["GlobalSettings"]):
			a = GlobalSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UserSettings"]):
			a = UserSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SessionService"]):
			a = SessionService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Sky"]):
			a = Sky()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Smoke"]):
			a = Smoke()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SnippetService"]):
			a = SnippetService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SocialService"]):
			a = SocialService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Sound"]):
			a = Sound()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SoundEffect"]):
			a = SoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["AssetSoundEffect"]):
			a = AssetSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ChorusSoundEffect"]):
			a = ChorusSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CompressorSoundEffect"]):
			a = CompressorSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CustomSoundEffect"]):
			a = CustomSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ChannelSelectorSoundEffect"]):
			a = ChannelSelectorSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DistortionSoundEffect"]):
			a = DistortionSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["EchoSoundEffect"]):
			a = EchoSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["EqualizerSoundEffect"]):
			a = EqualizerSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["FlangeSoundEffect"]):
			a = FlangeSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["PitchShiftSoundEffect"]):
			a = PitchShiftSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ReverbSoundEffect"]):
			a = ReverbSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TremoloSoundEffect"]):
			a = TremoloSoundEffect()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SoundGroup"]):
			a = SoundGroup()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SoundService"]):
			a = SoundService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Sparkles"]):
			a = Sparkles()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SpawnerService"]):
			a = SpawnerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Speaker"]):
			a = Speaker()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StackFrame"]):
			a = StackFrame()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StandalonePluginScripts"]):
			a = StandalonePluginScripts()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterGear"]):
			a = StarterGear()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterPack"]):
			a = StarterPack()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterPlayer"]):
			a = StarterPlayer()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterPlayerScripts"]):
			a = StarterPlayerScripts()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StarterCharacterScripts"]):
			a = StarterCharacterScripts()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Stats"]):
			a = Stats()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StatsItem"]):
			a = StatsItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RunningAverageItemDouble"]):
			a = RunningAverageItemDouble()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RunningAverageItemInt"]):
			a = RunningAverageItemInt()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RunningAverageTimeIntervalItem"]):
			a = RunningAverageTimeIntervalItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TotalCountTimeIntervalItem"]):
			a = TotalCountTimeIntervalItem()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StopWatchReporter"]):
			a = StopWatchReporter()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Studio"]):
			a = Studio()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioAssetService"]):
			a = StudioAssetService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioData"]):
			a = StudioData()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioDeviceEmulatorService"]):
			a = StudioDeviceEmulatorService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioHighDpiService"]):
			a = StudioHighDpiService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioPublishService"]):
			a = StudioPublishService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioScriptDebugEventListener"]):
			a = StudioScriptDebugEventListener()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioService"]):
			a = StudioService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StudioTheme"]):
			a = StudioTheme()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["SurfaceAppearance"]):
			a = SurfaceAppearance()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TaskScheduler"]):
			a = TaskScheduler()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Team"]):
			a = Team()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TeamCreateService"]):
			a = TeamCreateService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Teams"]):
			a = Teams()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TeleportAsyncResult"]):
			a = TeleportAsyncResult()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TeleportOptions"]):
			a = TeleportOptions()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TeleportService"]):
			a = TeleportService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TemporaryCageMeshProvider"]):
			a = TemporaryCageMeshProvider()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TemporaryScriptService"]):
			a = TemporaryScriptService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TerrainDetail"]):
			a = TerrainDetail()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TerrainRegion"]):
			a = TerrainRegion()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TestService"]):
			a = TestService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextBoxService"]):
			a = TextBoxService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChannel"]):
			a = TextChannel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChatCommand"]):
			a = TextChatCommand()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChatConfigurations"]):
			a = TextChatConfigurations()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BubbleChatConfiguration"]):
			a = BubbleChatConfiguration()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ChatInputBarConfiguration"]):
			a = ChatInputBarConfiguration()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ChatWindowConfiguration"]):
			a = ChatWindowConfiguration()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChatMessage"]):
			a = TextChatMessage()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChatMessageProperties"]):
			a = TextChatMessageProperties()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextChatService"]):
			a = TextChatService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextFilterResult"]):
			a = TextFilterResult()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextService"]):
			a = TextService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TextSource"]):
			a = TextSource()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ThirdPartyUserService"]):
			a = ThirdPartyUserService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ThreadState"]):
			a = ThreadState()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TimerService"]):
			a = TimerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ToastNotificationService"]):
			a = ToastNotificationService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TouchInputService"]):
			a = TouchInputService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TouchTransmitter"]):
			a = TouchTransmitter()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TracerService"]):
			a = TracerService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TrackerLodController"]):
			a = TrackerLodController()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TrackerStreamAnimation"]):
			a = TrackerStreamAnimation()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Trail"]):
			a = Trail()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Translator"]):
			a = Translator()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TweenBase"]):
			a = TweenBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Tween"]):
			a = Tween()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["TweenService"]):
			a = TweenService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UGCValidationService"]):
			a = UGCValidationService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIBase"]):
			a = UIBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIComponent"]):
			a = UIComponent()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIConstraint"]):
			a = UIConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIAspectRatioConstraint"]):
			a = UIAspectRatioConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UISizeConstraint"]):
			a = UISizeConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UITextSizeConstraint"]):
			a = UITextSizeConstraint()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UICorner"]):
			a = UICorner()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIGradient"]):
			a = UIGradient()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UILayout"]):
			a = UILayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIGridStyleLayout"]):
			a = UIGridStyleLayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIGridLayout"]):
			a = UIGridLayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIListLayout"]):
			a = UIListLayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIPageLayout"]):
			a = UIPageLayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UITableLayout"]):
			a = UITableLayout()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIPadding"]):
			a = UIPadding()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIScale"]):
			a = UIScale()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UIStroke"]):
			a = UIStroke()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UnvalidatedAssetService"]):
			a = UnvalidatedAssetService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UserGameSettings"]):
			a = UserGameSettings()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UserInputService"]):
			a = UserInputService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["UserService"]):
			a = UserService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VRService"]):
			a = VRService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ValueBase"]):
			a = ValueBase()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BinaryStringValue"]):
			a = BinaryStringValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BoolValue"]):
			a = BoolValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["BrickColorValue"]):
			a = BrickColorValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["CFrameValue"]):
			a = CFrameValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Color3Value"]):
			a = Color3Value()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["DoubleConstrainedValue"]):
			a = DoubleConstrainedValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["IntConstrainedValue"]):
			a = IntConstrainedValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["IntValue"]):
			a = IntValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["NumberValue"]):
			a = NumberValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["ObjectValue"]):
			a = ObjectValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["RayValue"]):
			a = RayValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["StringValue"]):
			a = StringValue()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Vector3Value"]):
			a = Vector3Value()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Vector3Curve"]):
			a = Vector3Curve()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VersionControlService"]):
			a = VersionControlService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VideoCaptureService"]):
			a = VideoCaptureService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VirtualInputManager"]):
			a = VirtualInputManager()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VirtualUser"]):
			a = VirtualUser()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VisibilityService"]):
			a = VisibilityService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["Visit"]):
			a = Visit()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VoiceChannel"]):
			a = VoiceChannel()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VoiceChatInternal"]):
			a = VoiceChatInternal()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VoiceChatService"]):
			a = VoiceChatService()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["VoiceSource"]):
			a = VoiceSource()
			if parent is not None:
				a.Parent = parent
			return a

		if isinstance(className, Literal["WeldConstraint"]):
			a = WeldConstraint()
			if parent is not None:
				a.Parent = parent
			return a

	@abstractmethod
	def ClearAllChildren(self) -> None:
		pass

	@abstractmethod
	def Clone(self) -> Self:
		pass

	@abstractmethod
	def Destroy(self) -> None:
		pass

	@abstractmethod
	def FindFirstAncestor(self, name: str) -> Self:
		pass

	@abstractmethod
	def FindFirstAncestorOfClass(self, className: str) -> Self:
		pass

	@abstractmethod
	def FindFirstAncestorWhichIsA(self, className: str) -> Self:
		pass

	@abstractmethod
	def FindFirstChild(self, name: str, recursive: bool) -> Self:
		pass

	@abstractmethod
	def FindFirstChildOfClass(self, className: str) -> Self:
		pass

	@abstractmethod
	def FindFirstChildWhichIsA(self, className: str, recursive: bool) -> Self:
		pass

	@abstractmethod
	def FindFirstDescendant(self, name: str) -> Self:
		pass

	@abstractmethod
	def GetActor(self) -> 'Actor':
		pass

	@abstractmethod
	def GetAttribute(self, attribute: str) -> Any:
		pass

	@abstractmethod
	def GetAttributeChangedSignal(self, attribute: str) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def GetAttributes(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetChildren(self) -> list[Self]:
		pass

	@abstractmethod
	def GetDebugId(self, scopeLength: int) -> str:
		pass

	@abstractmethod
	def GetDescendants(self) -> list[Any]:
		pass

	@abstractmethod
	def GetFullName(self) -> str:
		pass

	@abstractmethod
	def GetPropertyChangedSignal(self, property: str) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def IsA(self, className: str) -> bool:
		pass

	@abstractmethod
	def IsAncestorOf(self, descendant: Self) -> bool:
		pass

	@abstractmethod
	def IsDescendantOf(self, ancestor: Self) -> bool:
		pass

	@abstractmethod
	def Remove(self) -> None:
		pass

	@abstractmethod
	def SetAttribute(self, attribute: str, value: Any) -> None:
		pass

	@abstractmethod
	def WaitForChild(self, childName: str, timeOut: float) -> Self:
		pass

	@abstractmethod
	def children(self) -> list[Self]:
		pass

	@abstractmethod
	def clone(self) -> Self:
		pass

	@abstractmethod
	def destroy(self) -> None:
		pass

	@abstractmethod
	def findFirstChild(self, name: str, recursive: bool) -> Self:
		pass

	@abstractmethod
	def getChildren(self) -> list[Self]:
		pass

	@abstractmethod
	def isA(self, className: str) -> bool:
		pass

	@abstractmethod
	def isDescendantOf(self, ancestor: Self) -> bool:
		pass

	@abstractmethod
	def remove(self) -> None:
		pass


	pass

class Accoutrement(Instance):
	AttachmentForward: Vector3
	AttachmentPoint: CFrame
	AttachmentPos: Vector3
	AttachmentRight: Vector3
	AttachmentUp: Vector3

	pass

class Accessory(Accoutrement):
	AccessoryType: AccessoryType

	pass

class Hat(Accoutrement):

	pass

class AdPortal(Instance):
	PortalInvalidReason: str
	PortalStatus: AdPortalStatus
	PortalType: AdPortalType
	PortalVersion: int

	pass

class AdService(Instance):
	@abstractmethod
	def ShowVideoAd(self) -> None:
		pass


	pass

class AdvancedDragger(Instance):

	pass

class AnalyticsService(Instance):
	ApiKey: str
	@abstractmethod
	def FireCustomEvent(self, player: Instance, eventCategory: str, customData: Any) -> None:
		pass

	@abstractmethod
	def FireEvent(self, category: str, value: Any) -> None:
		pass

	@abstractmethod
	def FireInGameEconomyEvent(self, player: Instance, itemName: str, economyAction: AnalyticsEconomyAction, itemCategory: str, amount: int, currency: str, location: Any, customData: Any) -> None:
		pass

	@abstractmethod
	def FireLogEvent(self, player: Instance, logLevel: AnalyticsLogLevel, message: str, debugInfo: Any, customData: Any) -> None:
		pass

	@abstractmethod
	def FirePlayerProgressionEvent(self, player: Instance, category: str, progressionStatus: AnalyticsProgressionStatus, location: Any, statistics: Any, customData: Any) -> None:
		pass


	pass

class Animation(Instance):
	AnimationId: Content

	pass

class AnimationClip(Instance):
	Loop: bool
	Priority: AnimationPriority

	pass

class CurveAnimation(AnimationClip):

	pass

class KeyframeSequence(AnimationClip):
	AuthoredHipHeight: float
	@abstractmethod
	def AddKeyframe(self, keyframe: Instance) -> None:
		pass

	@abstractmethod
	def GetKeyframes(self) -> list[Instance]:
		pass

	@abstractmethod
	def RemoveKeyframe(self, keyframe: Instance) -> None:
		pass


	pass

class AnimationClipProvider(Instance):
	@abstractmethod
	def GetAnimationClip(self, assetId: Content) -> AnimationClip:
		pass

	@abstractmethod
	def GetAnimationClipById(self, assetId: int, useCache: bool) -> AnimationClip:
		pass

	@abstractmethod
	def GetMemStats(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def RegisterActiveAnimationClip(self, animationClip: AnimationClip) -> Content:
		pass

	@abstractmethod
	def RegisterAnimationClip(self, animationClip: AnimationClip) -> Content:
		pass

	@abstractmethod
	def GetAnimationClipAsync(self, assetId: Content) -> AnimationClip:
		pass

	@abstractmethod
	def GetAnimations(self, userId: int) -> Instance:
		pass


	pass

class AnimationController(Instance):
	@abstractmethod
	def GetPlayingAnimationTracks(self) -> list[Any]:
		pass

	@abstractmethod
	def LoadAnimation(self, animation: Animation) -> 'AnimationTrack':
		pass


	pass

class AnimationFromVideoCreatorService(Instance):
	@abstractmethod
	def CreateJob(self, filePath: str) -> str:
		pass

	@abstractmethod
	def DownloadJobResult(self, jobId: str, outputFilePath: str) -> str:
		pass

	@abstractmethod
	def FullProcess(self, videoFilePath: str, progressCallback: Callable[..., Any]) -> str:
		pass

	@abstractmethod
	def GetJobStatus(self, jobId: str) -> str:
		pass


	pass

class AnimationFromVideoCreatorStudioService(Instance):
	@abstractmethod
	def IsAgeRestricted(self) -> bool:
		pass

	@abstractmethod
	def CreateAnimationByUploadingVideo(self, progressCallback: Callable[..., Any]) -> str:
		pass

	@abstractmethod
	def ImportVideoWithPrompt(self) -> str:
		pass


	pass

class AnimationRigData(Instance):
	@abstractmethod
	def LoadFromHumanoid(self, humanoid: Instance) -> bool:
		pass


	pass

class AnimationStreamTrack(Instance):
	Animation: 'TrackerStreamAnimation'
	IsPlaying: bool
	Priority: AnimationPriority
	WeightCurrent: float
	WeightTarget: float
	@abstractmethod
	def AdjustWeight(self, weight: float, fadeTime: float) -> None:
		pass

	@abstractmethod
	def GetTrackerData(self) -> tuple[Any]:
		pass

	@abstractmethod
	def Play(self, fadeTime: float, weight: float) -> None:
		pass

	@abstractmethod
	def Stop(self, fadeTime: float) -> None:
		pass


	pass

class AnimationTrack(Instance):
	IsPlaying: bool
	Length: float
	Looped: bool
	Priority: AnimationPriority
	Speed: float
	TimePosition: float
	WeightCurrent: float
	WeightTarget: float
	Animation: Animation
	@abstractmethod
	def AdjustSpeed(self, speed: float) -> None:
		pass

	@abstractmethod
	def AdjustWeight(self, weight: float, fadeTime: float) -> None:
		pass

	@abstractmethod
	def GetMarkerReachedSignal(self, name: str) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def GetTimeOfKeyframe(self, keyframeName: str) -> float:
		pass

	@abstractmethod
	def Play(self, fadeTime: float, weight: float, speed: float) -> None:
		pass

	@abstractmethod
	def Stop(self, fadeTime: float) -> None:
		pass


	pass

class Animator(Instance):
	PreferLodEnabled: bool
	@abstractmethod
	def ApplyJointVelocities(self, motors: Any) -> None:
		pass

	@abstractmethod
	def GetPlayingAnimationTracks(self) -> list[Any]:
		pass

	@abstractmethod
	def GetPlayingAnimationTracksCoreScript(self) -> list[Any]:
		pass

	@abstractmethod
	def LoadAnimation(self, animation: Animation) -> AnimationTrack:
		pass

	@abstractmethod
	def LoadAnimationCoreScript(self, animation: Animation) -> AnimationTrack:
		pass

	@abstractmethod
	def LoadStreamAnimation(self, animation: 'TrackerStreamAnimation') -> AnimationStreamTrack:
		pass

	@abstractmethod
	def StepAnimations(self, deltaTime: float) -> None:
		pass


	pass

class AppUpdateService(Instance):
	@abstractmethod
	def CheckForUpdate(self, handler: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def DisableDUAR(self) -> None:
		pass

	@abstractmethod
	def DisableDUARAndOpenSurvey(self, surveyUrl: str) -> None:
		pass

	@abstractmethod
	def PerformManagedUpdate(self) -> bool:
		pass


	pass

class AssetCounterService(Instance):

	pass

class AssetDeliveryProxy(Instance):
	Interface: str
	Port: int
	StartServer: bool

	pass

class AssetImportService(Instance):
	@abstractmethod
	def PickFileWithPrompt(self) -> str:
		pass

	@abstractmethod
	def StartSessionWithPrompt(self) -> 'AssetImportSession':
		pass


	pass

class AssetImportSession(Instance):
	@abstractmethod
	def Cancel(self) -> None:
		pass

	@abstractmethod
	def GetCurrentStatusTable(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetFilename(self) -> str:
		pass

	@abstractmethod
	def GetInstance(self, nodeId: int) -> Instance:
		pass

	@abstractmethod
	def GetSettingsRoot(self) -> Instance:
		pass

	@abstractmethod
	def IsAvatar(self) -> bool:
		pass

	@abstractmethod
	def Upload(self) -> None:
		pass


	pass

class AssetManagerService(Instance):
	@abstractmethod
	def GetMeshIdFromAliasName(self, aliasName: str) -> int:
		pass

	@abstractmethod
	def GetMeshIdFromAssetId(self, assetId: int) -> int:
		pass

	@abstractmethod
	def GetTextureIdFromAliasName(self, aliasName: str) -> int:
		pass

	@abstractmethod
	def GetTextureIdFromAssetId(self, assetId: int) -> int:
		pass

	@abstractmethod
	def HasUnpublishedChangesForLinkedSource(self, aliasName: str) -> bool:
		pass

	@abstractmethod
	def InsertAudio(self, assetId: int, assetName: str) -> None:
		pass

	@abstractmethod
	def InsertImage(self, assetId: int) -> None:
		pass

	@abstractmethod
	def InsertLinkedSourceAsLocalScript(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def InsertLinkedSourceAsModuleScript(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def InsertLinkedSourceAsScript(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def InsertMesh(self, aliasName: str, insertWithLocation: bool) -> None:
		pass

	@abstractmethod
	def InsertMeshesWithLocation(self, aliasNames: list[Any]) -> None:
		pass

	@abstractmethod
	def InsertModel(self, modelId: int) -> None:
		pass

	@abstractmethod
	def InsertPackage(self, packageId: int) -> None:
		pass

	@abstractmethod
	def InsertVideo(self, assetId: int, assetName: str) -> None:
		pass

	@abstractmethod
	def OpenLinkedSource(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def OpenPlace(self, placeId: int) -> None:
		pass

	@abstractmethod
	def RefreshLinkedSource(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def RevertLinkedSourceToLastPublishedVersion(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def ShowPackageDetails(self, packageId: int) -> None:
		pass

	@abstractmethod
	def UpdateAllPackages(self, packageId: int) -> None:
		pass

	@abstractmethod
	def ViewPackageOnWebsite(self, packageId: int) -> None:
		pass

	@abstractmethod
	def AddNewPlace(self) -> int:
		pass

	@abstractmethod
	def CreateAlias(self, assetType: int, assetId: int, aliasName: str) -> None:
		pass

	@abstractmethod
	def DeleteAlias(self, aliasName: str) -> None:
		pass

	@abstractmethod
	def PublishLinkedSource(self, assetId: int, aliasName: str) -> None:
		pass

	@abstractmethod
	def RemovePlace(self, placeId: int) -> None:
		pass

	@abstractmethod
	def RenameAlias(self, assetType: int, assetId: int, oldAliasName: str, newAliasName: str) -> None:
		pass

	@abstractmethod
	def RenameModel(self, modelId: int, newName: str) -> None:
		pass

	@abstractmethod
	def RenamePlace(self, placeId: int, newName: str) -> None:
		pass


	pass

class AssetPatchSettings(Instance):
	ContentId: str
	OutputPath: str
	PatchId: str

	pass

class AssetService(Instance):
	@abstractmethod
	def GetBundleDetailsSync(self, bundleId: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def CreatePlaceAsync(self, placeName: str, templatePlaceID: int, description: str) -> int:
		pass

	@abstractmethod
	def CreatePlaceInPlayerInventoryAsync(self, player: Instance, placeName: str, templatePlaceID: int, description: str) -> int:
		pass

	@abstractmethod
	def GetAssetIdsForPackage(self, packageAssetId: int) -> list[Any]:
		pass

	@abstractmethod
	def GetAssetThumbnailAsync(self, assetId: int, thumbnailSize: Vector2, assetType: int) -> tuple[Any]:
		pass

	@abstractmethod
	def GetBundleDetailsAsync(self, bundleId: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetCreatorAssetID(self, creationID: int) -> int:
		pass

	@abstractmethod
	def GetGamePlacesAsync(self) -> Instance:
		pass

	@abstractmethod
	def SavePlaceAsync(self) -> None:
		pass


	pass

class Atmosphere(Instance):
	Color: Color3
	Decay: Color3
	Density: float
	Glare: float
	Haze: float
	Offset: float

	pass

class Attachment(Instance):
	Axis: Vector3
	Orientation: Vector3
	Position: Vector3
	Rotation: Vector3
	SecondaryAxis: Vector3
	Visible: bool
	WorldAxis: Vector3
	WorldCFrame: CFrame
	WorldOrientation: Vector3
	WorldPosition: Vector3
	WorldRotation: Vector3
	WorldSecondaryAxis: Vector3
	CFrame: CFrame
	@abstractmethod
	def GetAxis(self) -> Vector3:
		pass

	@abstractmethod
	def GetSecondaryAxis(self) -> Vector3:
		pass

	@abstractmethod
	def SetAxis(self, axis: Vector3) -> None:
		pass

	@abstractmethod
	def SetSecondaryAxis(self, axis: Vector3) -> None:
		pass


	pass

class Bone(Attachment):
	IsCFrameDriven: bool
	Transform: CFrame
	TransformedCFrame: CFrame
	TransformedWorldCFrame: CFrame

	pass

class AvatarEditorService(Instance):
	@abstractmethod
	def GetAccessoryType(self, avatarAssetType: AvatarAssetType) -> AccessoryType:
		pass

	@abstractmethod
	def NoPromptCreateOutfit(self, humanoidDescription: 'HumanoidDescription', rigType: HumanoidRigType, name: str) -> bool:
		pass

	@abstractmethod
	def NoPromptDeleteOutfit(self, outfitId: int) -> bool:
		pass

	@abstractmethod
	def NoPromptRenameOutfit(self, outfitId: int, name: str) -> bool:
		pass

	@abstractmethod
	def NoPromptSaveAvatar(self, humanoidDescription: 'HumanoidDescription', rigType: HumanoidRigType, saveDict: dict[Any, Any], gearAssetId: int) -> bool:
		pass

	@abstractmethod
	def NoPromptSetFavorite(self, itemId: int, itemType: AvatarItemType, shouldFavorite: bool) -> bool:
		pass

	@abstractmethod
	def NoPromptUpdateOutfit(self, outfitId: int, humanoidDescription: 'HumanoidDescription', rigType: HumanoidRigType) -> bool:
		pass

	@abstractmethod
	def PerformCreateOutfitWithDescription(self, humanoidDescription: 'HumanoidDescription', name: str) -> None:
		pass

	@abstractmethod
	def PerformDeleteOutfit(self) -> None:
		pass

	@abstractmethod
	def PerformRenameOutfit(self, name: str) -> None:
		pass

	@abstractmethod
	def PerformSaveAvatarWithDescription(self, humanoidDescription: 'HumanoidDescription', addedAssets: list[Any], removedAssets: list[Any]) -> None:
		pass

	@abstractmethod
	def PerformSetFavorite(self) -> None:
		pass

	@abstractmethod
	def PerformUpdateOutfit(self, humanoidDescription: 'HumanoidDescription') -> None:
		pass

	@abstractmethod
	def PromptAllowInventoryReadAccess(self) -> None:
		pass

	@abstractmethod
	def PromptCreateOutfit(self, outfit: 'HumanoidDescription', rigType: HumanoidRigType) -> None:
		pass

	@abstractmethod
	def PromptDeleteOutfit(self, outfitId: int) -> None:
		pass

	@abstractmethod
	def PromptRenameOutfit(self, outfitId: int) -> None:
		pass

	@abstractmethod
	def PromptSaveAvatar(self, humanoidDescription: 'HumanoidDescription', rigType: HumanoidRigType) -> None:
		pass

	@abstractmethod
	def PromptSetFavorite(self, itemId: int, itemType: AvatarItemType, shouldFavorite: bool) -> None:
		pass

	@abstractmethod
	def PromptUpdateOutfit(self, outfitId: int, updatedOutfit: 'HumanoidDescription', rigType: HumanoidRigType) -> None:
		pass

	@abstractmethod
	def SetAllowInventoryReadAccess(self, inventoryReadAccessGranted: bool) -> None:
		pass

	@abstractmethod
	def SignalCreateOutfitFailed(self) -> None:
		pass

	@abstractmethod
	def SignalCreateOutfitPermissionDenied(self) -> None:
		pass

	@abstractmethod
	def SignalDeleteOutfitFailed(self) -> None:
		pass

	@abstractmethod
	def SignalDeleteOutfitPermissionDenied(self) -> None:
		pass

	@abstractmethod
	def SignalRenameOutfitFailed(self) -> None:
		pass

	@abstractmethod
	def SignalRenameOutfitPermissionDenied(self) -> None:
		pass

	@abstractmethod
	def SignalSaveAvatarFailed(self) -> None:
		pass

	@abstractmethod
	def SignalSaveAvatarPermissionDenied(self) -> None:
		pass

	@abstractmethod
	def SignalSetFavoriteFailed(self) -> None:
		pass

	@abstractmethod
	def SignalSetFavoritePermissionDenied(self) -> None:
		pass

	@abstractmethod
	def SignalUpdateOutfitFailed(self) -> None:
		pass

	@abstractmethod
	def SignalUpdateOutfitPermissionDenied(self) -> None:
		pass

	@abstractmethod
	def CheckApplyDefaultClothing(self, humanoidDescription: 'HumanoidDescription') -> 'HumanoidDescription':
		pass

	@abstractmethod
	def ConformToAvatarRules(self, humanoidDescription: 'HumanoidDescription') -> 'HumanoidDescription':
		pass

	@abstractmethod
	def GetAvatarRules(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetBatchItemDetails(self, itemIds: list[Any], itemType: AvatarItemType) -> list[Any]:
		pass

	@abstractmethod
	def GetFavorite(self, itemId: int, itemType: AvatarItemType) -> bool:
		pass

	@abstractmethod
	def GetInventory(self, assetTypes: list[Any]) -> 'InventoryPages':
		pass

	@abstractmethod
	def GetItemDetails(self, itemId: int, itemType: AvatarItemType) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetOutfits(self, outfitSource: OutfitSource, outfitType: OutfitType) -> 'OutfitPages':
		pass

	@abstractmethod
	def GetRecommendedAssets(self, assetType: AvatarAssetType, contextAssetId: int) -> list[Any]:
		pass

	@abstractmethod
	def GetRecommendedAssetsV2(self, assetType: AvatarAssetType, assetId: int, numItems: int, includeDetails: bool) -> list[Any]:
		pass

	@abstractmethod
	def GetRecommendedBundles(self, bundleId: int) -> list[Any]:
		pass

	@abstractmethod
	def GetRecommendedBundlesV2(self, bundleType: BundleType, bundleId: int, numItems: int, includeDetails: bool) -> list[Any]:
		pass

	@abstractmethod
	def SearchCatalog(self, searchParameters: 'CatalogSearchParams') -> 'CatalogPages':
		pass


	pass

class AvatarImportService(Instance):
	@abstractmethod
	def ImportFBXAnimationFromFilePathUserMayChooseModel(self, fbxFilePath: str, selectedRig: Instance, userChooseModelThenImportCB: Callable[..., Any]) -> Instance:
		pass

	@abstractmethod
	def ImportFBXAnimationUserMayChooseModel(self, selectedRig: Instance, userChooseModelThenImportCB: Callable[..., Any]) -> Instance:
		pass

	@abstractmethod
	def ImportFbxRigWithoutSceneLoad(self, isR15: bool) -> Instance:
		pass

	@abstractmethod
	def ImportLoadedFBXAnimation(self, useFBXModel: bool) -> Instance:
		pass

	@abstractmethod
	def LoadRigAndDetectType(self, promptR15Callback: Callable[..., Any]) -> Instance:
		pass


	pass

class Backpack(Instance):

	pass

class BackpackItem(Instance):
	TextureId: Content

	pass

class HopperBin(BackpackItem):
	Active: bool
	BinType: BinType
	@abstractmethod
	def Disable(self) -> None:
		pass

	@abstractmethod
	def ToggleSelect(self) -> None:
		pass


	pass

class Tool(BackpackItem):
	CanBeDropped: bool
	Enabled: bool
	Grip: CFrame
	GripForward: Vector3
	GripPos: Vector3
	GripRight: Vector3
	GripUp: Vector3
	ManualActivationOnly: bool
	RequiresHandle: bool
	ToolTip: str
	@abstractmethod
	def Activate(self) -> None:
		pass

	@abstractmethod
	def Deactivate(self) -> None:
		pass


	pass

class Flag(Tool):
	TeamColor: BrickColor

	pass

class BadgeService(Instance):
	@abstractmethod
	def AwardBadge(self, userId: int, badgeId: int) -> bool:
		pass

	@abstractmethod
	def GetBadgeInfoAsync(self, badgeId: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def IsDisabled(self, badgeId: int) -> bool:
		pass

	@abstractmethod
	def IsLegal(self, badgeId: int) -> bool:
		pass

	@abstractmethod
	def UserHasBadge(self, userId: int, badgeId: int) -> bool:
		pass

	@abstractmethod
	def UserHasBadgeAsync(self, userId: int, badgeId: int) -> bool:
		pass


	pass

class BasePlayerGui(Instance):
	@abstractmethod
	def GetGuiObjectsAtPosition(self, x: int, y: int) -> list[Instance]:
		pass

	@abstractmethod
	def GetGuiObjectsInCircle(self, position: Vector2, radius: float) -> list[Instance]:
		pass


	pass

class CoreGui(BasePlayerGui):
	SelectionImageObject: 'GuiObject'
	Version: int
	@abstractmethod
	def SetUserGuiRendering(self, enabled: bool, guiAdornee: Instance, faceId: NormalId) -> None:
		pass

	@abstractmethod
	def TakeScreenshot(self) -> None:
		pass

	@abstractmethod
	def ToggleRecording(self) -> None:
		pass


	pass

class PlayerGui(BasePlayerGui):
	CurrentScreenOrientation: ScreenOrientation
	SelectionImageObject: 'GuiObject'
	ScreenOrientation: ScreenOrientation
	@abstractmethod
	def GetTopbarTransparency(self) -> float:
		pass

	@abstractmethod
	def SetTopbarTransparency(self, transparency: float) -> None:
		pass


	pass

class StarterGui(BasePlayerGui):
	ProcessUserInput: bool
	ResetPlayerGuiOnSpawn: bool
	ShowDevelopmentGui: bool
	ScreenOrientation: ScreenOrientation
	VirtualCursorMode: VirtualCursorMode
	@abstractmethod
	def GetCoreGuiEnabled(self, coreGuiType: CoreGuiType) -> bool:
		pass

	@abstractmethod
	def RegisterGetCore(self, parameterName: str, getFunction: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def RegisterSetCore(self, parameterName: str, setFunction: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def SetCore(self, parameterName: str, value: Any) -> None:
		pass

	@abstractmethod
	def SetCoreGuiEnabled(self, coreGuiType: CoreGuiType, enabled: bool) -> None:
		pass

	@abstractmethod
	def GetCore(self, parameterName: str) -> Any:
		pass


	pass

class BaseWrap(Instance):
	CageMeshId: Content
	CageOrigin: CFrame
	CageOriginWorld: CFrame
	HSRAssetId: Content
	ImportOrigin: CFrame
	ImportOriginWorld: CFrame
	@abstractmethod
	def GetFaces(self, cageType: CageType) -> list[Any]:
		pass

	@abstractmethod
	def GetVertices(self, cageType: CageType) -> list[Any]:
		pass

	@abstractmethod
	def IsHSRReady(self) -> bool:
		pass

	@abstractmethod
	def ModifyVertices(self, cageType: CageType, vertices: list[Any]) -> None:
		pass


	pass

class WrapLayer(BaseWrap):
	AutoSkin: WrapLayerAutoSkin
	BindOffset: CFrame
	Color: Color3
	DebugMode: WrapLayerDebugMode
	Enabled: bool
	Order: int
	Puffiness: float
	ReferenceMeshId: Content
	ReferenceOrigin: CFrame
	ReferenceOriginWorld: CFrame
	ShrinkFactor: float

	pass

class WrapTarget(BaseWrap):
	Color: Color3
	DebugMode: WrapTargetDebugMode
	Stiffness: float

	pass

class Beam(Instance):
	Attachment0: Attachment
	Attachment1: Attachment
	Brightness: float
	Color: ColorSequence
	CurveSize0: float
	CurveSize1: float
	Enabled: bool
	FaceCamera: bool
	LightEmission: float
	LightInfluence: float
	Segments: int
	Texture: Content
	TextureLength: float
	TextureSpeed: float
	Transparency: NumberSequence
	Width0: float
	Width1: float
	ZOffset: float
	TextureMode: TextureMode
	@abstractmethod
	def SetTextureOffset(self, offset: float) -> None:
		pass


	pass

class BindableEvent(Instance):
	@abstractmethod
	def Fire(self, arguments: tuple[Any]) -> None:
		pass


	pass

class BindableFunction(Instance):
	@abstractmethod
	def Invoke(self, arguments: tuple[Any]) -> tuple[Any]:
		pass


	pass

class BodyMover(Instance):

	pass

class BodyAngularVelocity(BodyMover):
	AngularVelocity: Vector3
	MaxTorque: Vector3
	P: float
	angularvelocity: Vector3
	maxTorque: Vector3

	pass

class BodyForce(BodyMover):
	Force: Vector3
	force: Vector3

	pass

class BodyGyro(BodyMover):
	D: float
	MaxTorque: Vector3
	P: float
	cframe: CFrame
	maxTorque: Vector3
	CFrame: CFrame

	pass

class BodyPosition(BodyMover):
	D: float
	MaxForce: Vector3
	P: float
	Position: Vector3
	maxForce: Vector3
	position: Vector3
	@abstractmethod
	def GetLastForce(self) -> Vector3:
		pass

	@abstractmethod
	def lastForce(self) -> Vector3:
		pass


	pass

class BodyThrust(BodyMover):
	Force: Vector3
	Location: Vector3
	force: Vector3
	location: Vector3

	pass

class BodyVelocity(BodyMover):
	MaxForce: Vector3
	P: float
	Velocity: Vector3
	maxForce: Vector3
	velocity: Vector3
	@abstractmethod
	def GetLastForce(self) -> Vector3:
		pass

	@abstractmethod
	def lastForce(self) -> Vector3:
		pass


	pass

class RocketPropulsion(BodyMover):
	CartoonFactor: float
	MaxSpeed: float
	MaxThrust: float
	MaxTorque: Vector3
	Target: 'BasePart'
	TargetOffset: Vector3
	TargetRadius: float
	ThrustD: float
	ThrustP: float
	TurnD: float
	TurnP: float
	@abstractmethod
	def Abort(self) -> None:
		pass

	@abstractmethod
	def Fire(self) -> None:
		pass

	@abstractmethod
	def fire(self) -> None:
		pass


	pass

class Breakpoint(Instance):
	Condition: str
	ContinueExecution: bool
	Enabled: bool
	Id: int
	Line: int
	LogMessage: str
	MetaBreakpointId: int
	Script: str
	Valid: bool
	Verified: bool

	pass

class BrowserService(Instance):
	@abstractmethod
	def CloseBrowserWindow(self) -> None:
		pass

	@abstractmethod
	def CopyAuthCookieFromBrowserToEngine(self) -> None:
		pass

	@abstractmethod
	def EmitHybridEvent(self, moduleName: str, eventName: str, params: str) -> None:
		pass

	@abstractmethod
	def ExecuteJavaScript(self, javascript: str) -> None:
		pass

	@abstractmethod
	def OpenBrowserWindow(self, url: str) -> None:
		pass

	@abstractmethod
	def OpenNativeOverlay(self, title: str, url: str) -> None:
		pass

	@abstractmethod
	def OpenWeChatAuthWindow(self) -> None:
		pass

	@abstractmethod
	def ReturnToJavaScript(self, callbackId: str, success: bool, params: str) -> None:
		pass

	@abstractmethod
	def SendCommand(self, command: str) -> None:
		pass


	pass

class BulkImportService(Instance):
	@abstractmethod
	def LaunchBulkImport(self, assetTypeToImport: int) -> None:
		pass

	@abstractmethod
	def ShowBulkImportView(self) -> None:
		pass


	pass

class CacheableContentProvider(Instance):

	pass

class HSRDataContentProvider(CacheableContentProvider):

	pass

class MeshContentProvider(CacheableContentProvider):
	@abstractmethod
	def GetContentMemoryData(self) -> dict[Any, Any]:
		pass


	pass

class SolidModelContentProvider(CacheableContentProvider):

	pass

class CalloutService(Instance):
	@abstractmethod
	def AttachCallout(self, definitionId: str, locationId: str, target: Instance) -> None:
		pass

	@abstractmethod
	def DefineCallout(self, definitionId: str, title: str, description: str, learnMoreURL: str) -> None:
		pass

	@abstractmethod
	def DetachCalloutsByDefinitionId(self, definitionId: str) -> None:
		pass


	pass

class Camera(Instance):
	CameraSubject: Instance
	CoordinateFrame: CFrame
	DiagonalFieldOfView: float
	FieldOfView: float
	Focus: CFrame
	HeadLocked: bool
	HeadScale: float
	MaxAxisFieldOfView: float
	NearPlaneZ: float
	ViewportSize: Vector2
	focus: CFrame
	CFrame: CFrame
	CameraType: CameraType
	FieldOfViewMode: FieldOfViewMode
	@abstractmethod
	def GetLargestCutoffDistance(self, ignoreList: list[Instance]) -> float:
		pass

	@abstractmethod
	def GetPanSpeed(self) -> float:
		pass

	@abstractmethod
	def GetPartsObscuringTarget(self, castPoints: list[Any], ignoreList: list[Instance]) -> list[Instance]:
		pass

	@abstractmethod
	def GetRenderCFrame(self) -> 'CFrame':
		pass

	@abstractmethod
	def GetRoll(self) -> float:
		pass

	@abstractmethod
	def GetTiltSpeed(self) -> float:
		pass

	@abstractmethod
	def Interpolate(self, endPos: 'CFrame', endFocus: 'CFrame', duration: float) -> None:
		pass

	@abstractmethod
	def PanUnits(self, units: int) -> None:
		pass

	@abstractmethod
	def ScreenPointToRay(self, x: float, y: float, depth: float) -> Ray:
		pass

	@abstractmethod
	def SetCameraPanMode(self, mode: CameraPanMode) -> None:
		pass

	@abstractmethod
	def SetImageServerView(self, modelCoord: 'CFrame') -> None:
		pass

	@abstractmethod
	def SetRoll(self, rollAngle: float) -> None:
		pass

	@abstractmethod
	def TiltUnits(self, units: int) -> bool:
		pass

	@abstractmethod
	def ViewportPointToRay(self, x: float, y: float, depth: float) -> Ray:
		pass

	@abstractmethod
	def WorldToScreenPoint(self, worldPoint: Vector3) -> tuple[Any]:
		pass

	@abstractmethod
	def WorldToViewportPoint(self, worldPoint: Vector3) -> tuple[Any]:
		pass

	@abstractmethod
	def Zoom(self, distance: float) -> bool:
		pass


	pass

class ChangeHistoryService(Instance):
	@abstractmethod
	def GetCanRedo(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetCanUndo(self) -> tuple[Any]:
		pass

	@abstractmethod
	def Redo(self) -> None:
		pass

	@abstractmethod
	def ResetWaypoints(self) -> None:
		pass

	@abstractmethod
	def SetEnabled(self, state: bool) -> None:
		pass

	@abstractmethod
	def SetWaypoint(self, name: str) -> None:
		pass

	@abstractmethod
	def Undo(self) -> None:
		pass


	pass

class CharacterAppearance(Instance):

	pass

class BodyColors(CharacterAppearance):
	HeadColor: BrickColor
	HeadColor3: Color3
	LeftArmColor: BrickColor
	LeftArmColor3: Color3
	LeftLegColor: BrickColor
	LeftLegColor3: Color3
	RightArmColor: BrickColor
	RightArmColor3: Color3
	RightLegColor: BrickColor
	RightLegColor3: Color3
	TorsoColor: BrickColor
	TorsoColor3: Color3

	pass

class CharacterMesh(CharacterAppearance):
	BaseTextureId: int
	MeshId: int
	OverlayTextureId: int
	BodyPart: BodyPart

	pass

class Clothing(CharacterAppearance):
	Color3: Color3

	pass

class Pants(Clothing):
	PantsTemplate: Content

	pass

class Shirt(Clothing):
	ShirtTemplate: Content

	pass

class ShirtGraphic(CharacterAppearance):
	Graphic: Content
	Color3: Color3

	pass

class Skin(CharacterAppearance):
	SkinColor: BrickColor

	pass

class Chat(Instance):
	BubbleChatEnabled: bool
	LoadDefaultChat: bool
	@abstractmethod
	def Chat(self, partOrCharacter: Instance, message: str, color: ChatColor) -> None:
		pass

	@abstractmethod
	def ChatLocal(self, partOrCharacter: Instance, message: str, color: ChatColor) -> None:
		pass

	@abstractmethod
	def GetShouldUseLuaChat(self) -> bool:
		pass

	@abstractmethod
	def InvokeChatCallback(self, callbackType: ChatCallbackType, callbackArguments: tuple[Any]) -> tuple[Any]:
		pass

	@abstractmethod
	def RegisterChatCallback(self, callbackType: ChatCallbackType, callbackFunction: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def SetBubbleChatSettings(self, settings: Any) -> None:
		pass

	@abstractmethod
	def CanUserChatAsync(self, userId: int) -> bool:
		pass

	@abstractmethod
	def CanUsersChatAsync(self, userIdFrom: int, userIdTo: int) -> bool:
		pass

	@abstractmethod
	def FilterStringAsync(self, stringToFilter: str, playerFrom: 'Player', playerTo: 'Player') -> str:
		pass

	@abstractmethod
	def FilterStringForBroadcast(self, stringToFilter: str, playerFrom: 'Player') -> str:
		pass

	@abstractmethod
	def FilterStringForPlayerAsync(self, stringToFilter: str, playerToFilterFor: 'Player') -> str:
		pass


	pass

class ClickDetector(Instance):
	CursorIcon: Content
	MaxActivationDistance: float

	pass

class Clouds(Instance):
	Color: Color3
	Cover: float
	Density: float
	Enabled: bool

	pass

class ClusterPacketCache(Instance):

	pass

class CollectionService(Instance):
	@abstractmethod
	def AddTag(self, instance: Instance, tag: str) -> None:
		pass

	@abstractmethod
	def GetAllTags(self) -> list[Any]:
		pass

	@abstractmethod
	def GetCollection(self, className: str) -> list[Instance]:
		pass

	@abstractmethod
	def GetInstanceAddedSignal(self, tag: str) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def GetInstanceRemovedSignal(self, tag: str) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def GetTagged(self, tag: str) -> list[Instance]:
		pass

	@abstractmethod
	def GetTags(self, instance: Instance) -> list[Any]:
		pass

	@abstractmethod
	def HasTag(self, instance: Instance, tag: str) -> bool:
		pass

	@abstractmethod
	def RemoveTag(self, instance: Instance, tag: str) -> None:
		pass


	pass

class CommandInstance(Instance):
	AllowGUIAccessPoints: bool
	Checked: bool
	DefaultShortcut: str
	DisplayName: str
	Enabled: bool
	Icon: str
	Name: str
	Permission: CommandPermission
	StatusTip: str
	@abstractmethod
	def EnableGuiAccess(self, displayName: str, statusTip: str, defaultShortcut: str) -> None:
		pass

	@abstractmethod
	def RegisterExecutionCallback(self, callbackFunction: Callable[..., Any]) -> None:
		pass


	pass

class CommandService(Instance):
	@abstractmethod
	def Execute(self, name: str, params: Any) -> Any:
		pass

	@abstractmethod
	def RegisterCommand(self, plugin: 'Plugin', name: str, context: str, permission: CommandPermission) -> CommandInstance:
		pass


	pass

class Configuration(Instance):

	pass

class ConfigureServerService(Instance):

	pass

class Constraint(Instance):
	Active: bool
	Attachment0: Attachment
	Attachment1: Attachment
	Color: BrickColor
	Enabled: bool
	Visible: bool

	pass

class AlignOrientation(Constraint):
	MaxAngularVelocity: float
	MaxTorque: float
	Mode: OrientationAlignmentMode
	PrimaryAxis: Vector3
	PrimaryAxisOnly: bool
	ReactionTorqueEnabled: bool
	Responsiveness: float
	RigidityEnabled: bool
	SecondaryAxis: Vector3
	AlignType: AlignType
	CFrame: CFrame

	pass

class AlignPosition(Constraint):
	ApplyAtCenterOfMass: bool
	MaxForce: float
	MaxVelocity: float
	Mode: PositionAlignmentMode
	Position: Vector3
	ReactionForceEnabled: bool
	Responsiveness: float
	RigidityEnabled: bool

	pass

class AngularVelocity(Constraint):
	AngularVelocity: Vector3
	MaxTorque: float
	ReactionTorqueEnabled: bool
	RelativeTo: ActuatorRelativeTo

	pass

class AnimationConstraint(Constraint):
	MaxForce: float
	MaxTorque: float
	Transform: CFrame

	pass

class BallSocketConstraint(Constraint):
	LimitsEnabled: bool
	MaxFrictionTorque: float
	Radius: float
	Restitution: float
	TwistLimitsEnabled: bool
	TwistLowerAngle: float
	TwistUpperAngle: float
	UpperAngle: float

	pass

class HingeConstraint(Constraint):
	AngularResponsiveness: float
	AngularSpeed: float
	AngularVelocity: float
	CurrentAngle: float
	LimitsEnabled: bool
	LowerAngle: float
	MotorMaxAcceleration: float
	MotorMaxTorque: float
	Radius: float
	Restitution: float
	ServoMaxTorque: float
	TargetAngle: float
	UpperAngle: float
	ActuatorType: ActuatorType

	pass

class LineForce(Constraint):
	ApplyAtCenterOfMass: bool
	InverseSquareLaw: bool
	Magnitude: float
	MaxForce: float
	ReactionForceEnabled: bool

	pass

class LinearVelocity(Constraint):
	LineDirection: Vector3
	LineVelocity: float
	MaxForce: float
	PlaneVelocity: Vector2
	PrimaryTangentAxis: Vector3
	RelativeTo: ActuatorRelativeTo
	SecondaryTangentAxis: Vector3
	VectorVelocity: Vector3
	VelocityConstraintMode: VelocityConstraintMode

	pass

class PlaneConstraint(Constraint):

	pass

class Plane(PlaneConstraint):

	pass

class RigidConstraint(Constraint):

	pass

class RodConstraint(Constraint):
	CurrentDistance: float
	Length: float
	LimitAngle0: float
	LimitAngle1: float
	LimitsEnabled: bool
	Thickness: float

	pass

class RopeConstraint(Constraint):
	CurrentDistance: float
	Length: float
	Restitution: float
	Thickness: float
	WinchEnabled: bool
	WinchForce: float
	WinchResponsiveness: float
	WinchSpeed: float
	WinchTarget: float

	pass

class SlidingBallConstraint(Constraint):
	CurrentPosition: float
	LimitsEnabled: bool
	LinearResponsiveness: float
	LowerLimit: float
	MotorMaxAcceleration: float
	MotorMaxForce: float
	Restitution: float
	ServoMaxForce: float
	Size: float
	Speed: float
	TargetPosition: float
	UpperLimit: float
	Velocity: float
	ActuatorType: ActuatorType

	pass

class CylindricalConstraint(SlidingBallConstraint):
	AngularActuatorType: ActuatorType
	AngularLimitsEnabled: bool
	AngularResponsiveness: float
	AngularRestitution: float
	AngularSpeed: float
	AngularVelocity: float
	CurrentAngle: float
	InclinationAngle: float
	LowerAngle: float
	MotorMaxAngularAcceleration: float
	MotorMaxTorque: float
	RotationAxisVisible: bool
	ServoMaxTorque: float
	TargetAngle: float
	UpperAngle: float
	WorldRotationAxis: Vector3

	pass

class PrismaticConstraint(SlidingBallConstraint):

	pass

class SpringConstraint(Constraint):
	Coils: float
	CurrentLength: float
	Damping: float
	FreeLength: float
	LimitsEnabled: bool
	MaxForce: float
	MaxLength: float
	MinLength: float
	Radius: float
	Stiffness: float
	Thickness: float

	pass

class Torque(Constraint):
	RelativeTo: ActuatorRelativeTo
	Torque: Vector3

	pass

class TorsionSpringConstraint(Constraint):
	Coils: float
	CurrentAngle: float
	Damping: float
	LimitEnabled: bool
	LimitsEnabled: bool
	MaxAngle: float
	MaxTorque: float
	Radius: float
	Restitution: float
	Stiffness: float

	pass

class UniversalConstraint(Constraint):
	LimitsEnabled: bool
	MaxAngle: float
	Radius: float
	Restitution: float

	pass

class VectorForce(Constraint):
	ApplyAtCenterOfMass: bool
	Force: Vector3
	RelativeTo: ActuatorRelativeTo

	pass

class ContentProvider(Instance):
	BaseUrl: str
	RequestQueueSize: int
	@abstractmethod
	def CalculateNumTrianglesInMeshSync(self, meshId: str) -> int:
		pass

	@abstractmethod
	def GetDetailedFailedRequests(self) -> list[Any]:
		pass

	@abstractmethod
	def GetFailedRequests(self) -> list[Any]:
		pass

	@abstractmethod
	def ListEncryptedAssets(self) -> list[Any]:
		pass

	@abstractmethod
	def Preload(self, contentId: Content) -> None:
		pass

	@abstractmethod
	def RegisterDefaultEncryptionKey(self, encryptionKey: str) -> None:
		pass

	@abstractmethod
	def RegisterDefaultSessionKey(self, sessionKey: str) -> None:
		pass

	@abstractmethod
	def RegisterEncryptedAsset(self, assetId: Content, encryptionKey: str) -> None:
		pass

	@abstractmethod
	def RegisterSessionEncryptedAsset(self, contentId: Content, sessionKey: str) -> None:
		pass

	@abstractmethod
	def SetBaseUrl(self, url: str) -> None:
		pass

	@abstractmethod
	def UnregisterDefaultEncryptionKey(self) -> None:
		pass

	@abstractmethod
	def UnregisterEncryptedAsset(self, assetId: Content) -> None:
		pass

	@abstractmethod
	def CalculateNumTrianglesInMesh(self, meshId: str) -> int:
		pass

	@abstractmethod
	def PreloadAsync(self, contentIdList: list[Any], callbackFunction: Callable[..., Any]) -> None:
		pass


	pass

class ContextActionService(Instance):
	@abstractmethod
	def BindAction(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]) -> None:
		pass

	@abstractmethod
	def BindActionAtPriority(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, priorityLevel: int, inputTypes: tuple[Any]) -> None:
		pass

	@abstractmethod
	def BindActionToInputTypes(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]) -> None:
		pass

	@abstractmethod
	def BindActivate(self, userInputTypeForActivation: UserInputType, keyCodesForActivation: tuple[Any]) -> None:
		pass

	@abstractmethod
	def BindCoreAction(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]) -> None:
		pass

	@abstractmethod
	def BindCoreActionAtPriority(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, priorityLevel: int, inputTypes: tuple[Any]) -> None:
		pass

	@abstractmethod
	def CallFunction(self, actionName: str, state: UserInputState, inputObject: Instance) -> tuple[Any]:
		pass

	@abstractmethod
	def FireActionButtonFoundSignal(self, actionName: str, actionButton: Instance) -> None:
		pass

	@abstractmethod
	def GetAllBoundActionInfo(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetAllBoundCoreActionInfo(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetBoundActionInfo(self, actionName: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetBoundCoreActionInfo(self, actionName: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetCurrentLocalToolIcon(self) -> str:
		pass

	@abstractmethod
	def SetDescription(self, actionName: str, description: str) -> None:
		pass

	@abstractmethod
	def SetImage(self, actionName: str, image: str) -> None:
		pass

	@abstractmethod
	def SetPosition(self, actionName: str, position: UDim2) -> None:
		pass

	@abstractmethod
	def SetTitle(self, actionName: str, title: str) -> None:
		pass

	@abstractmethod
	def UnbindAction(self, actionName: str) -> None:
		pass

	@abstractmethod
	def UnbindActivate(self, userInputTypeForActivation: UserInputType, keyCodeForActivation: KeyCode) -> None:
		pass

	@abstractmethod
	def UnbindAllActions(self) -> None:
		pass

	@abstractmethod
	def UnbindCoreAction(self, actionName: str) -> None:
		pass

	@abstractmethod
	def GetButton(self, actionName: str) -> Instance:
		pass


	pass

class Controller(Instance):
	@abstractmethod
	def BindButton(self, button: Button, caption: str) -> None:
		pass

	@abstractmethod
	def GetButton(self, button: Button) -> bool:
		pass

	@abstractmethod
	def UnbindButton(self, button: Button) -> None:
		pass

	@abstractmethod
	def bindButton(self, button: Button, caption: str) -> None:
		pass

	@abstractmethod
	def getButton(self, button: Button) -> bool:
		pass


	pass

class HumanoidController(Controller):

	pass

class SkateboardController(Controller):
	Steer: float
	Throttle: float

	pass

class VehicleController(Controller):

	pass

class ControllerBase(Instance):
	MoveSpeedFactor: float
	RigidityEnabled: bool

	pass

class AirController(ControllerBase):
	CancelAirMomentum: bool
	MoveMaxForce: float
	OrientationMaxTorque: float
	OrientationSpeedFactor: float
	VectorForce: Vector3

	pass

class ClimbController(ControllerBase):
	AccelerationTime: float
	MoveMaxForce: float
	OrientationMaxTorque: float
	OrientationSpeedFactor: float

	pass

class GroundController(ControllerBase):
	AccelerationLean: float
	AccelerationTime: float
	AlignSpeed: float
	AlignTorque: float
	DecelerationTime: float
	Friction: float
	FrictionWeight: float
	GroundOffset: float
	MaxSlopeAngle: float
	StandForce: float
	StandSpeed: float
	TurningFactor: float

	pass

class SwimController(ControllerBase):
	AccelerationTime: float
	PitchMaxTorque: float
	PitchSpeedFactor: float
	RollMaxTorque: float
	RollSpeedFactor: float

	pass

class ControllerManager(Instance):
	ActiveController: ControllerBase
	BaseMoveSpeed: float
	BaseTurnSpeed: float
	FacingDirection: Vector3
	HipHeight: float
	MovingDirection: Vector3
	@abstractmethod
	def GetControllers(self) -> list[Instance]:
		pass


	pass

class ControllerService(Instance):

	pass

class CookiesService(Instance):

	pass

class CorePackages(Instance):

	pass

class CoreScriptSyncService(Instance):
	@abstractmethod
	def GetScriptFilePath(self, script: Instance) -> Any:
		pass


	pass

class CrossDMScriptChangeListener(Instance):
	@abstractmethod
	def IsWatchingScriptLine(self, scriptRef: str, lineNumber: int) -> bool:
		pass

	@abstractmethod
	def StartWatchingScriptLine(self, scriptRef: str, debuggerConnectionId: int, lineNumber: int) -> None:
		pass


	pass

class CustomEvent(Instance):
	@abstractmethod
	def GetAttachedReceivers(self) -> list[Instance]:
		pass

	@abstractmethod
	def SetValue(self, newValue: float) -> None:
		pass


	pass

class CustomEventReceiver(Instance):
	Source: Instance
	@abstractmethod
	def GetCurrentValue(self) -> float:
		pass


	pass

class DataModelMesh(Instance):
	Offset: Vector3
	Scale: Vector3
	VertexColor: Vector3

	pass

class BevelMesh(DataModelMesh):

	pass

class BlockMesh(BevelMesh):

	pass

class CylinderMesh(BevelMesh):

	pass

class FileMesh(DataModelMesh):
	MeshId: Content
	TextureId: Content

	pass

class SpecialMesh(FileMesh):
	MeshType: MeshType

	pass

class DataModelPatchService(Instance):
	@abstractmethod
	def GetPatch(self, patchName: str) -> Instance:
		pass

	@abstractmethod
	def RegisterPatch(self, patchName: str, behaviorName: str, localConfigPath: str, userId: int) -> None:
		pass

	@abstractmethod
	def UpdatePatch(self, userId: int, patchName: str, callbackFunction: Callable[..., Any]) -> None:
		pass


	pass

class DataModelSession(Instance):
	CurrentDataModelType: StudioDataModelType
	SessionId: str

	pass

class DataStoreIncrementOptions(Instance):
	@abstractmethod
	def GetMetadata(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def SetMetadata(self, attributes: dict[Any, Any]) -> None:
		pass


	pass

class DataStoreInfo(Instance):
	CreatedTime: int
	DataStoreName: str
	UpdatedTime: int

	pass

class DataStoreKey(Instance):
	KeyName: str

	pass

class DataStoreKeyInfo(Instance):
	CreatedTime: int
	UpdatedTime: int
	Version: str
	@abstractmethod
	def GetMetadata(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetUserIds(self) -> list[Any]:
		pass


	pass

class DataStoreObjectVersionInfo(Instance):
	CreatedTime: int
	IsDeleted: bool
	Version: str

	pass

class DataStoreOptions(Instance):
	AllScopes: bool
	@abstractmethod
	def SetExperimentalFeatures(self, experimentalFeatures: dict[Any, Any]) -> None:
		pass


	pass

class DataStoreService(Instance):
	AutomaticRetry: bool
	LegacyNamingScheme: bool
	@abstractmethod
	def GetDataStore(self, name: str, scope: str, options: Instance) -> 'GlobalDataStore':
		pass

	@abstractmethod
	def GetGlobalDataStore(self) -> 'GlobalDataStore':
		pass

	@abstractmethod
	def GetOrderedDataStore(self, name: str, scope: str) -> 'OrderedDataStore':
		pass

	@abstractmethod
	def GetRequestBudgetForRequestType(self, requestType: DataStoreRequestType) -> int:
		pass

	@abstractmethod
	def ListDataStoresAsync(self, prefix: str, pageSize: int, cursor: str) -> 'DataStoreListingPages':
		pass


	pass

class DataStoreSetOptions(Instance):
	@abstractmethod
	def GetMetadata(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def SetMetadata(self, attributes: dict[Any, Any]) -> None:
		pass


	pass

class Debris(Instance):
	MaxItems: int
	@abstractmethod
	def AddItem(self, item: Instance, lifetime: float) -> None:
		pass

	@abstractmethod
	def SetLegacyMaxItems(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def addItem(self, item: Instance, lifetime: float) -> None:
		pass


	pass

class DebugSettings(Instance):
	DataModel: int
	InstanceCount: int
	IsScriptStackTracingEnabled: bool
	JobCount: int
	PlayerCount: int
	ReportSoundWarnings: bool
	RobloxVersion: str
	TickCountPreciseOverride: TickCountSampleMethod

	pass

class DebuggablePluginWatcher(Instance):

	pass

class DebuggerBreakpoint(Instance):
	Condition: str
	ContinueExecution: bool
	IsEnabled: bool
	Line: int
	LogExpression: str
	isContextDependentBreakpoint: bool

	pass

class DebuggerConnection(Instance):
	ErrorMessage: str
	HasError: bool
	Id: int
	IsPaused: bool
	@abstractmethod
	def AddBreakpoint(self, script: str, line: int, breakpoint: Breakpoint) -> None:
		pass

	@abstractmethod
	def Close(self) -> None:
		pass

	@abstractmethod
	def EvaluateWatch(self, expression: str, frame: 'StackFrame', callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def GetFrameById(self, id: int) -> 'StackFrame':
		pass

	@abstractmethod
	def GetSource(self, scriptRef: str, status: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def GetThreadById(self, id: int) -> 'ThreadState':
		pass

	@abstractmethod
	def GetThreads(self, callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def GetVariableById(self, id: int) -> 'DebuggerVariable':
		pass

	@abstractmethod
	def Pause(self, thread: 'ThreadState', status: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def Populate(self, instance: Instance, callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def RemoveBreakpoint(self, breakpoint: Breakpoint) -> None:
		pass

	@abstractmethod
	def Resume(self, thread: 'ThreadState', status: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def SetExceptionBreakMode(self, breakMode: DebuggerExceptionBreakMode, callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def SetVariable(self, variable: 'DebuggerVariable', value: str, callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def Step(self, thread: 'ThreadState', callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def StepIn(self, thread: 'ThreadState', callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def StepOut(self, thread: 'ThreadState', callback: Callable[..., Any]) -> int:
		pass

	@abstractmethod
	def UpdateSelectedFrame(self, threadId: int, frameNumber: int) -> None:
		pass


	pass

class LocalDebuggerConnection(DebuggerConnection):

	pass

class DebuggerConnectionManager(Instance):
	Timeout: float
	@abstractmethod
	def ConnectLocal(self, dataModel: 'DataModel') -> int:
		pass

	@abstractmethod
	def ConnectRemote(self, host: str, port: int) -> int:
		pass

	@abstractmethod
	def FocusConnection(self, connection: DebuggerConnection) -> None:
		pass

	@abstractmethod
	def GetConnectionById(self, id: int) -> DebuggerConnection:
		pass


	pass

class DebuggerLuaResponse(Instance):
	IsError: bool
	IsSuccess: bool
	Message: str
	RequestId: int
	Status: DebuggerStatus
	@abstractmethod
	def GetArg(self) -> Any:
		pass


	pass

class DebuggerManager(Instance):
	DebuggingEnabled: bool
	@abstractmethod
	def AddDebugger(self, script: Instance) -> Instance:
		pass

	@abstractmethod
	def EnableDebugging(self) -> None:
		pass

	@abstractmethod
	def GetDebuggers(self) -> list[Instance]:
		pass

	@abstractmethod
	def Resume(self) -> None:
		pass

	@abstractmethod
	def StepIn(self) -> None:
		pass

	@abstractmethod
	def StepOut(self) -> None:
		pass

	@abstractmethod
	def StepOver(self) -> None:
		pass


	pass

class DebuggerUIService(Instance):
	@abstractmethod
	def EditBreakpoint(self, metaBreakpointId: int) -> None:
		pass

	@abstractmethod
	def EditWatch(self, expression: str) -> None:
		pass

	@abstractmethod
	def IsConnectionForPlayDataModel(self, debuggerConnectionId: int) -> bool:
		pass

	@abstractmethod
	def OpenScriptAtLine(self, guid: str, debuggerConnectionId: int, line: int, showErrorOnFail: bool) -> None:
		pass

	@abstractmethod
	def Pause(self) -> None:
		pass

	@abstractmethod
	def RemoveScriptLineMarkers(self, debuggerConnectionId: int, allMarkers: bool) -> None:
		pass

	@abstractmethod
	def Resume(self) -> None:
		pass

	@abstractmethod
	def SetCurrentFrameId(self, debuggerThreadId: int, debuggerFrameId: int) -> None:
		pass

	@abstractmethod
	def SetCurrentThreadId(self, debuggerThreadId: int) -> None:
		pass

	@abstractmethod
	def SetScriptLineMarker(self, guid: str, debuggerConnectionId: int, line: int, lineMarkerType: bool) -> None:
		pass


	pass

class DebuggerVariable(Instance):
	Name: str
	Populated: bool
	Type: str
	Value: str
	VariableId: int
	VariablesCount: int
	@abstractmethod
	def GetVariableByIndex(self, index: int) -> Self:
		pass

	@abstractmethod
	def GetVariableByName(self, name: str) -> Self:
		pass


	pass

class DebuggerWatch(Instance):
	Expression: str

	pass

class DeviceIdService(Instance):
	@abstractmethod
	def GetDeviceId(self) -> str:
		pass


	pass

class Dialog(Instance):
	BehaviorType: DialogBehaviorType
	ConversationDistance: float
	GoodbyeChoiceActive: bool
	GoodbyeDialog: str
	InUse: bool
	InitialPrompt: str
	Purpose: DialogPurpose
	Tone: DialogTone
	TriggerDistance: float
	TriggerOffset: Vector3
	@abstractmethod
	def GetCurrentPlayers(self) -> list[Instance]:
		pass

	@abstractmethod
	def SetPlayerIsUsing(self, player: Instance, isUsing: bool) -> None:
		pass

	@abstractmethod
	def SignalDialogChoiceSelected(self, player: Instance, dialogChoice: Instance) -> None:
		pass


	pass

class DialogChoice(Instance):
	GoodbyeChoiceActive: bool
	GoodbyeDialog: str
	ResponseDialog: str
	UserDialog: str

	pass

class DraftsService(Instance):
	@abstractmethod
	def DiscardEdits(self, scripts: list[Instance]) -> None:
		pass

	@abstractmethod
	def GetDraftStatus(self, script: Instance) -> DraftStatusCode:
		pass

	@abstractmethod
	def GetEditors(self, script: Instance) -> list[Instance]:
		pass

	@abstractmethod
	def RestoreScripts(self, scripts: list[Instance]) -> None:
		pass

	@abstractmethod
	def ShowDiffsAgainstBase(self, scripts: list[Instance]) -> None:
		pass

	@abstractmethod
	def ShowDiffsAgainstServer(self, scripts: list[Instance]) -> None:
		pass

	@abstractmethod
	def CommitEdits(self, scripts: list[Instance]) -> None:
		pass

	@abstractmethod
	def GetDrafts(self) -> list[Instance]:
		pass

	@abstractmethod
	def UpdateToLatestVersion(self, scripts: list[Instance]) -> None:
		pass


	pass

class Dragger(Instance):
	@abstractmethod
	def AxisRotate(self, axis: Axis) -> None:
		pass

	@abstractmethod
	def MouseDown(self, mousePart: Instance, pointOnMousePart: Vector3, parts: list[Instance]) -> None:
		pass

	@abstractmethod
	def MouseMove(self, mouseRay: Ray) -> None:
		pass

	@abstractmethod
	def MouseUp(self) -> None:
		pass


	pass

class DraggerService(Instance):
	AlignDraggedObjects: bool
	AngleSnapEnabled: bool
	AngleSnapIncrement: float
	AnimateHover: bool
	CollisionsEnabled: bool
	GeometrySnapColor: Color3
	HoverAnimateFrequency: float
	HoverLineThickness: int
	HoverThickness: float
	JointsEnabled: bool
	LinearSnapEnabled: bool
	LinearSnapIncrement: float
	PivotSnapToGeometry: bool
	ShowHover: bool
	ShowPivotIndicator: bool
	DraggerCoordinateSpace: DraggerCoordinateSpace
	DraggerMovementMode: DraggerMovementMode

	pass

class EulerRotationCurve(Instance):
	RotationOrder: RotationOrder
	@abstractmethod
	def GetAnglesAtTime(self, time: float) -> list[Any]:
		pass

	@abstractmethod
	def GetRotationAtTime(self, time: float) -> CFrame:
		pass

	@abstractmethod
	def X(self) -> 'FloatCurve':
		pass

	@abstractmethod
	def Y(self) -> 'FloatCurve':
		pass

	@abstractmethod
	def Z(self) -> 'FloatCurve':
		pass


	pass

class EventIngestService(Instance):
	@abstractmethod
	def SendEventDeferred(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SendEventImmediately(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SetRBXEvent(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SetRBXEventStream(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass


	pass

class ExperienceInviteOptions(Instance):
	InviteMessageId: int
	InviteUser: int
	LaunchData: str
	PromptMessage: str

	pass

class Explosion(Instance):
	BlastPressure: float
	BlastRadius: float
	DestroyJointRadiusPercent: float
	Position: Vector3
	TimeScale: float
	Visible: bool
	ExplosionType: ExplosionType

	pass

class FaceAnimatorService(Instance):
	AudioAnimationEnabled: bool
	FlipHeadOrientation: bool
	VideoAnimationEnabled: bool
	@abstractmethod
	def GetTrackerLodController(self) -> 'TrackerLodController':
		pass

	@abstractmethod
	def Init(self, videoEnabled: bool, audioEnabled: bool) -> None:
		pass

	@abstractmethod
	def IsStarted(self) -> bool:
		pass

	@abstractmethod
	def Start(self) -> None:
		pass

	@abstractmethod
	def Step(self) -> None:
		pass

	@abstractmethod
	def Stop(self) -> None:
		pass


	pass

class FaceControls(Instance):
	ChinRaiser: float
	ChinRaiserUpperLip: float
	Corrugator: float
	EyesLookDown: float
	EyesLookLeft: float
	EyesLookRight: float
	EyesLookUp: float
	FlatPucker: float
	Funneler: float
	JawDrop: float
	JawLeft: float
	JawRight: float
	LeftBrowLowerer: float
	LeftCheekPuff: float
	LeftCheekRaiser: float
	LeftDimpler: float
	LeftEyeClosed: float
	LeftEyeUpperLidRaiser: float
	LeftInnerBrowRaiser: float
	LeftLipCornerDown: float
	LeftLipCornerPuller: float
	LeftLipStretcher: float
	LeftLowerLipDepressor: float
	LeftNoseWrinkler: float
	LeftOuterBrowRaiser: float
	LeftUpperLipRaiser: float
	LipPresser: float
	LipsTogether: float
	LowerLipSuck: float
	MouthLeft: float
	MouthRight: float
	Pucker: float
	RightBrowLowerer: float
	RightCheekPuff: float
	RightCheekRaiser: float
	RightDimpler: float
	RightEyeClosed: float
	RightEyeUpperLidRaiser: float
	RightInnerBrowRaiser: float
	RightLipCornerDown: float
	RightLipCornerPuller: float
	RightLipStretcher: float
	RightLowerLipDepressor: float
	RightNoseWrinkler: float
	RightOuterBrowRaiser: float
	RightUpperLipRaiser: float
	TongueDown: float
	TongueOut: float
	TongueUp: float
	UpperLipSuck: float

	pass

class FaceInstance(Instance):
	Face: NormalId

	pass

class Decal(FaceInstance):
	LocalTransparencyModifier: float
	Shiny: float
	Specular: float
	Texture: Content
	Transparency: float
	ZIndex: int
	Color3: Color3

	pass

class Texture(Decal):
	OffsetStudsU: float
	OffsetStudsV: float
	StudsPerTileU: float
	StudsPerTileV: float

	pass

class FacialAnimationRecordingService(Instance):
	BiometricDataConsent: bool
	@abstractmethod
	def IsAgeRestricted(self) -> bool:
		pass

	@abstractmethod
	def CheckOrRequestCameraPermission(self) -> str:
		pass


	pass

class FacialAnimationStreamingService(Instance):
	EnableFlags: FacialAnimationFlags
	Enabled: bool

	pass

class FacialAnimationStreamingServiceV2(Instance):
	ServiceState: int
	@abstractmethod
	def IsAudioEnabled(self, mask: int) -> bool:
		pass

	@abstractmethod
	def IsPlaceEnabled(self, mask: int) -> bool:
		pass

	@abstractmethod
	def IsServerEnabled(self, mask: int) -> bool:
		pass

	@abstractmethod
	def IsVideoEnabled(self, mask: int) -> bool:
		pass

	@abstractmethod
	def ResolveStateForUser(self, userId: int) -> int:
		pass


	pass

class Feature(Instance):
	FaceId: NormalId
	InOut: InOut
	LeftRight: LeftRight
	TopBottom: TopBottom

	pass

class Hole(Feature):

	pass

class MotorFeature(Feature):

	pass

class File(Instance):
	Size: int
	@abstractmethod
	def GetBinaryContents(self) -> str:
		pass

	@abstractmethod
	def GetTemporaryId(self) -> Content:
		pass


	pass

class Fire(Instance):
	Color: Color3
	Enabled: bool
	Heat: float
	SecondaryColor: Color3
	Size: float
	TimeScale: float
	size: float
	@abstractmethod
	def FastForward(self, numFrames: int) -> None:
		pass


	pass

class FlagStandService(Instance):

	pass

class FloatCurve(Instance):
	Length: int
	@abstractmethod
	def GetKeyAtIndex(self, index: int) -> 'FloatCurveKey':
		pass

	@abstractmethod
	def GetKeyIndicesAtTime(self, time: float) -> list[Any]:
		pass

	@abstractmethod
	def GetKeys(self) -> list[Any]:
		pass

	@abstractmethod
	def GetValueAtTime(self, time: float) -> float| None:
		pass

	@abstractmethod
	def InsertKey(self, key: 'FloatCurveKey') -> list[Any]:
		pass

	@abstractmethod
	def RemoveKeyAtIndex(self, startingIndex: int, count: int) -> int:
		pass

	@abstractmethod
	def SetKeys(self, keys: list[Any]) -> int:
		pass


	pass

class FlyweightService(Instance):

	pass

class CSGDictionaryService(FlyweightService):

	pass

class NonReplicatedCSGDictionaryService(FlyweightService):

	pass

class Folder(Instance):

	pass

class ForceField(Instance):
	Visible: bool

	pass

class FriendService(Instance):
	@abstractmethod
	def GetPlatformFriends(self) -> list[Any]:
		pass


	pass

class FunctionalTest(Instance):
	Description: str
	@abstractmethod
	def Error(self, message: str) -> None:
		pass

	@abstractmethod
	def Failed(self, message: str) -> None:
		pass

	@abstractmethod
	def Pass(self, message: str) -> None:
		pass

	@abstractmethod
	def Passed(self, message: str) -> None:
		pass

	@abstractmethod
	def Warn(self, message: str) -> None:
		pass


	pass

class GamePassService(Instance):
	@abstractmethod
	def PlayerHasPass(self, player: 'Player', gamePassId: int) -> bool:
		pass


	pass

class GameSettings(Instance):
	VideoCaptureEnabled: bool
	VideoRecording: bool

	pass

class GamepadService(Instance):
	GamepadCursorEnabled: bool
	@abstractmethod
	def DisableGamepadCursor(self) -> None:
		pass

	@abstractmethod
	def EnableGamepadCursor(self, guiObject: Instance) -> None:
		pass

	@abstractmethod
	def GetGamepadCursorPosition(self) -> Vector2:
		pass

	@abstractmethod
	def SetGamepadCursorPosition(self, position: Vector2) -> None:
		pass


	pass

class Geometry(Instance):

	pass

class GetTextBoundsParams(Instance):
	Size: float
	Text: str
	Width: float
	Font: Font

	pass

class GlobalDataStore(Instance):
	@abstractmethod
	def OnUpdate(self, key: str, callback: Callable[..., Any]) -> 'RBXScriptConnection':
		pass

	@abstractmethod
	def GetAsync(self, key: str) -> tuple[Any]:
		pass

	@abstractmethod
	def IncrementAsync(self, key: str, delta: int, userIds: list[Any], options: DataStoreIncrementOptions) -> Any:
		pass

	@abstractmethod
	def RemoveAsync(self, key: str) -> tuple[Any]:
		pass

	@abstractmethod
	def SetAsync(self, key: str, value: Any, userIds: list[Any], options: DataStoreSetOptions) -> Any:
		pass

	@abstractmethod
	def UpdateAsync(self, key: str, transformFunction: Callable[..., Any]) -> tuple[Any]:
		pass


	pass

class DataStore(GlobalDataStore):
	@abstractmethod
	def GetVersionAsync(self, key: str, version: str) -> tuple[Any]:
		pass

	@abstractmethod
	def ListKeysAsync(self, prefix: str, pageSize: int, cursor: str) -> 'DataStoreKeyPages':
		pass

	@abstractmethod
	def ListVersionsAsync(self, key: str, sortDirection: SortDirection, minDate: int, maxDate: int, pageSize: int) -> 'DataStoreVersionPages':
		pass

	@abstractmethod
	def RemoveVersionAsync(self, key: str, version: str) -> None:
		pass


	pass

class OrderedDataStore(GlobalDataStore):
	@abstractmethod
	def GetSortedAsync(self, ascending: bool, pagesize: int, minValue: Any, maxValue: Any) -> Instance:
		pass


	pass

class GoogleAnalyticsConfiguration(Instance):

	pass

class GroupService(Instance):
	@abstractmethod
	def GetAlliesAsync(self, groupId: int) -> 'StandardPages':
		pass

	@abstractmethod
	def GetEnemiesAsync(self, groupId: int) -> 'StandardPages':
		pass

	@abstractmethod
	def GetGroupInfoAsync(self, groupId: int) -> Any:
		pass

	@abstractmethod
	def GetGroupsAsync(self, userId: int) -> list[Any]:
		pass


	pass

class GuiBase(Instance):

	pass

class GuiBase2d(GuiBase):
	AbsolutePosition: Vector2
	AbsoluteRotation: float
	AbsoluteSize: Vector2
	AutoLocalize: bool
	ClippedRect: Rect
	IsNotOccluded: bool
	Localize: bool
	RawRect2D: Rect
	RootLocalizationTable: 'LocalizationTable'
	SelectionBehaviorDown: SelectionBehavior
	SelectionBehaviorLeft: SelectionBehavior
	SelectionBehaviorRight: SelectionBehavior
	SelectionBehaviorUp: SelectionBehavior
	SelectionGroup: bool
	TotalGroupScale: float

	pass

class GuiObject(GuiBase2d):
	Active: bool
	AnchorPoint: Vector2
	BackgroundColor: BrickColor
	BackgroundColor3: Color3
	BackgroundTransparency: float
	BorderColor: BrickColor
	BorderColor3: Color3
	BorderSizePixel: int
	ClipsDescendants: bool
	Draggable: bool
	LayoutOrder: int
	NextSelectionDown: 'GuiObject'
	NextSelectionLeft: 'GuiObject'
	NextSelectionRight: 'GuiObject'
	NextSelectionUp: 'GuiObject'
	Position: UDim2
	Rotation: float
	Selectable: bool
	SelectionImageObject: 'GuiObject'
	SelectionOrder: int
	Size: UDim2
	Transparency: float
	Visible: bool
	ZIndex: int
	AutomaticSize: AutomaticSize
	BorderMode: BorderMode
	SizeConstraint: SizeConstraint
	@abstractmethod
	def TweenPosition(self, endPosition: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]) -> bool:
		pass

	@abstractmethod
	def TweenSize(self, endSize: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]) -> bool:
		pass

	@abstractmethod
	def TweenSizeAndPosition(self, endSize: UDim2, endPosition: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]) -> bool:
		pass


	pass

class CanvasGroup(GuiObject):
	GroupColor3: Color3
	GroupTransparency: float

	pass

class Frame(GuiObject):
	Style: FrameStyle

	pass

class GuiButton(GuiObject):
	AutoButtonColor: bool
	Modal: bool
	Selected: bool
	Style: ButtonStyle

	pass

class ImageButton(GuiButton):
	ContentImageSize: Vector2
	HoverImage: Content
	Image: Content
	ImageColor3: Color3
	ImageRectOffset: Vector2
	ImageRectSize: Vector2
	ImageTransparency: float
	IsLoaded: bool
	PressedImage: Content
	ResampleMode: ResamplerMode
	SliceCenter: Rect
	SliceScale: float
	TileSize: UDim2
	ScaleType: ScaleType
	@abstractmethod
	def SetEnableContentImageSizeChangedEvents(self, enabled: bool) -> None:
		pass


	pass

class TextButton(GuiButton):
	ContentText: str
	FontFace: Font
	LineHeight: float
	LocalizedText: str
	MaxVisibleGraphemes: int
	RichText: bool
	Text: str
	TextBounds: Vector2
	TextColor: BrickColor
	TextColor3: Color3
	TextFits: bool
	TextScaled: bool
	TextSize: float
	TextStrokeColor3: Color3
	TextStrokeTransparency: float
	TextTransparency: float
	TextWrap: bool
	TextWrapped: bool
	Font: Font
	FontSize: FontSize
	TextTruncate: TextTruncate
	TextXAlignment: TextXAlignment
	TextYAlignment: TextYAlignment
	@abstractmethod
	def SetTextFromInput(self, text: str) -> None:
		pass


	pass

class GuiLabel(GuiObject):

	pass

class ImageLabel(GuiLabel):
	ContentImageSize: Vector2
	Image: Content
	ImageColor3: Color3
	ImageRectOffset: Vector2
	ImageRectSize: Vector2
	ImageTransparency: float
	IsLoaded: bool
	ResampleMode: ResamplerMode
	SliceCenter: Rect
	SliceScale: float
	TileSize: UDim2
	ScaleType: ScaleType
	@abstractmethod
	def SetEnableContentImageSizeChangedEvents(self, enabled: bool) -> None:
		pass


	pass

class TextLabel(GuiLabel):
	ContentText: str
	FontFace: Font
	LineHeight: float
	LocalizedText: str
	MaxVisibleGraphemes: int
	RichText: bool
	Text: str
	TextBounds: Vector2
	TextColor: BrickColor
	TextColor3: Color3
	TextFits: bool
	TextScaled: bool
	TextSize: float
	TextStrokeColor3: Color3
	TextStrokeTransparency: float
	TextTransparency: float
	TextWrap: bool
	TextWrapped: bool
	Font: Font
	FontSize: FontSize
	TextTruncate: TextTruncate
	TextXAlignment: TextXAlignment
	TextYAlignment: TextYAlignment
	@abstractmethod
	def SetTextFromInput(self, text: str) -> None:
		pass


	pass

class ScrollingFrame(GuiObject):
	AbsoluteCanvasSize: Vector2
	AbsoluteWindowSize: Vector2
	AutomaticCanvasSize: AutomaticSize
	BottomImage: Content
	CanvasPosition: Vector2
	CanvasSize: UDim2
	HorizontalBarRect: Rect
	HorizontalScrollBarInset: ScrollBarInset
	MaxCanvasPosition: Vector2
	MidImage: Content
	ScrollBarImageColor3: Color3
	ScrollBarImageTransparency: float
	ScrollBarThickness: int
	ScrollVelocity: Vector2
	ScrollingEnabled: bool
	TopImage: Content
	VerticalBarRect: Rect
	VerticalScrollBarInset: ScrollBarInset
	ElasticBehavior: ElasticBehavior
	ScrollingDirection: ScrollingDirection
	VerticalScrollBarPosition: VerticalScrollBarPosition
	@abstractmethod
	def ClearInertialScrolling(self) -> None:
		pass

	@abstractmethod
	def GetSampledInertialVelocity(self) -> Vector2:
		pass

	@abstractmethod
	def ScrollToTop(self) -> None:
		pass


	pass

class TextBox(GuiObject):
	ClearTextOnFocus: bool
	ContentText: str
	CursorPosition: int
	FontFace: Font
	LineHeight: float
	ManualFocusRelease: bool
	MaxVisibleGraphemes: int
	MultiLine: bool
	OverlayNativeInput: bool
	PlaceholderColor3: Color3
	PlaceholderText: str
	RichText: bool
	SelectionStart: int
	ShowNativeInput: bool
	Text: str
	TextBounds: Vector2
	TextColor: BrickColor
	TextColor3: Color3
	TextEditable: bool
	TextFits: bool
	TextScaled: bool
	TextSize: float
	TextStrokeColor3: Color3
	TextStrokeTransparency: float
	TextTransparency: float
	TextWrap: bool
	TextWrapped: bool
	Font: Font
	FontSize: FontSize
	ReturnKeyType: ReturnKeyType
	TextInputType: TextInputType
	TextTruncate: TextTruncate
	TextXAlignment: TextXAlignment
	TextYAlignment: TextYAlignment
	@abstractmethod
	def CaptureFocus(self) -> None:
		pass

	@abstractmethod
	def IsFocused(self) -> bool:
		pass

	@abstractmethod
	def ReleaseFocus(self, submitted: bool) -> None:
		pass

	@abstractmethod
	def ResetKeyboardMode(self) -> None:
		pass

	@abstractmethod
	def SetTextFromInput(self, text: str) -> None:
		pass


	pass

class VideoFrame(GuiObject):
	IsLoaded: bool
	Looped: bool
	Playing: bool
	Resolution: Vector2
	TimeLength: float
	TimePosition: float
	Video: Content
	Volume: float
	@abstractmethod
	def Pause(self) -> None:
		pass

	@abstractmethod
	def Play(self) -> None:
		pass


	pass

class ViewportFrame(GuiObject):
	Ambient: Color3
	CurrentCamera: Camera
	ImageColor3: Color3
	ImageTransparency: float
	IsMirrored: bool
	LightColor: Color3
	LightDirection: Vector3

	pass

class LayerCollector(GuiBase2d):
	Enabled: bool
	ResetOnSpawn: bool
	ZIndexBehavior: ZIndexBehavior
	@abstractmethod
	def GetLayoutNodeTree(self) -> dict[Any, Any]:
		pass


	pass

class BillboardGui(LayerCollector):
	Active: bool
	Adornee: Instance
	AlwaysOnTop: bool
	Brightness: float
	ClipsDescendants: bool
	CurrentDistance: float
	DistanceLowerLimit: float
	DistanceStep: float
	DistanceUpperLimit: float
	ExtentsOffset: Vector3
	ExtentsOffsetWorldSpace: Vector3
	LightInfluence: float
	MaxDistance: float
	PlayerToHideFrom: Instance
	Size: UDim2
	SizeOffset: Vector2
	StudsOffset: Vector3
	StudsOffsetWorldSpace: Vector3
	@abstractmethod
	def GetScreenSpaceBounds(self) -> Any:
		pass


	pass

class PluginGui(LayerCollector):
	Title: str
	@abstractmethod
	def BindToClose(self, function: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def GetRelativeMousePosition(self) -> Vector2:
		pass


	pass

class DockWidgetPluginGui(PluginGui):
	HostWidgetWasRestored: bool
	@abstractmethod
	def RequestRaise(self) -> None:
		pass


	pass

class QWidgetPluginGui(PluginGui):

	pass

class ScreenGui(LayerCollector):
	ClipToDeviceSafeArea: bool
	DisplayOrder: int
	IgnoreGuiInset: bool
	OnTopOfCoreBlur: bool
	SafeAreaCompatibility: SafeAreaCompatibility

	pass

class GuiMain(ScreenGui):

	pass

class SurfaceGuiBase(LayerCollector):
	Active: bool
	Adornee: Instance
	Face: NormalId

	pass

class AdGui(SurfaceGuiBase):
	AdShape: AdShape

	pass

class SurfaceGui(SurfaceGuiBase):
	AlwaysOnTop: bool
	Brightness: float
	CanvasSize: Vector2
	ClipsDescendants: bool
	LightInfluence: float
	PixelsPerStud: float
	SizingMode: SurfaceGuiSizingMode
	ToolPunchThroughDistance: float
	ZOffset: float

	pass

class GuiBase3d(GuiBase):
	Color: BrickColor
	Transparency: float
	Visible: bool
	Color3: Color3

	pass

class FloorWire(GuiBase3d):
	CycleOffset: float
	From: 'BasePart'
	StudsBetweenTextures: float
	Texture: Content
	TextureSize: Vector2
	To: 'BasePart'
	Velocity: float
	WireRadius: float

	pass

class InstanceAdornment(GuiBase3d):
	Adornee: Instance

	pass

class SelectionBox(InstanceAdornment):
	LineThickness: float
	SurfaceColor: BrickColor
	SurfaceColor3: Color3
	SurfaceTransparency: float

	pass

class PVAdornment(GuiBase3d):
	Adornee: 'PVInstance'

	pass

class HandleAdornment(PVAdornment):
	AlwaysOnTop: bool
	SizeRelativeOffset: Vector3
	ZIndex: int
	AdornCullingMode: AdornCullingMode
	CFrame: CFrame

	pass

class BoxHandleAdornment(HandleAdornment):
	Size: Vector3

	pass

class ConeHandleAdornment(HandleAdornment):
	Height: float
	Radius: float

	pass

class CylinderHandleAdornment(HandleAdornment):
	Angle: float
	Height: float
	InnerRadius: float
	Radius: float

	pass

class ImageHandleAdornment(HandleAdornment):
	Image: Content
	Size: Vector2

	pass

class LineHandleAdornment(HandleAdornment):
	Length: float
	Thickness: float

	pass

class SphereHandleAdornment(HandleAdornment):
	Radius: float

	pass

class WireframeHandleAdornment(HandleAdornment):
	@abstractmethod
	def AddLine(self, from_: Vector3, to: Vector3) -> None:
		pass

	@abstractmethod
	def AddLines(self, points: list[Any]) -> None:
		pass

	@abstractmethod
	def AddPath(self, points: list[Any], loop: bool) -> None:
		pass

	@abstractmethod
	def Clear(self) -> None:
		pass


	pass

class ParabolaAdornment(PVAdornment):
	A: float
	B: float
	C: float
	Range: float
	Thickness: float
	@abstractmethod
	def FindPartOnParabola(self, ignoreDescendentsTable: list[Instance]) -> tuple[Any]:
		pass


	pass

class SelectionSphere(PVAdornment):
	SurfaceColor: BrickColor
	SurfaceColor3: Color3
	SurfaceTransparency: float

	pass

class PartAdornment(GuiBase3d):
	Adornee: 'BasePart'

	pass

class HandlesBase(PartAdornment):

	pass

class ArcHandles(HandlesBase):
	Axes: Axes

	pass

class Handles(HandlesBase):
	Style: HandlesStyle
	Faces: Faces

	pass

class SurfaceSelection(PartAdornment):
	TargetSurface: NormalId

	pass

class SelectionLasso(GuiBase3d):
	Humanoid: 'Humanoid'

	pass

class SelectionPartLasso(SelectionLasso):
	Part: 'BasePart'

	pass

class SelectionPointLasso(SelectionLasso):
	Point: Vector3

	pass

class GuiService(Instance):
	AutoSelectGuiEnabled: bool
	CoreEffectFolder: Folder
	CoreGuiFolder: Folder
	CoreGuiNavigationEnabled: bool
	GuiNavigationEnabled: bool
	IsModalDialog: bool
	IsWindows: bool
	MenuIsOpen: bool
	SelectedCoreObject: GuiObject
	SelectedObject: GuiObject
	TouchControlsEnabled: bool
	@abstractmethod
	def AddCenterDialog(self, dialog: Instance, centerDialogType: CenterDialogType, showFunction: Callable[..., Any], hideFunction: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def AddKey(self, key: str) -> None:
		pass

	@abstractmethod
	def AddSelectionParent(self, selectionName: str, selectionParent: Instance) -> None:
		pass

	@abstractmethod
	def AddSelectionTuple(self, selectionName: str, selections: tuple[Any]) -> None:
		pass

	@abstractmethod
	def AddSpecialKey(self, key: SpecialKey) -> None:
		pass

	@abstractmethod
	def BroadcastNotification(self, data: str, notificationType: int) -> None:
		pass

	@abstractmethod
	def ClearError(self) -> None:
		pass

	@abstractmethod
	def CloseInspectMenu(self) -> None:
		pass

	@abstractmethod
	def CloseStatsBasedOnInputString(self, input: str) -> bool:
		pass

	@abstractmethod
	def ForceTenFootInterface(self, isForced: bool) -> None:
		pass

	@abstractmethod
	def GetBrickCount(self) -> int:
		pass

	@abstractmethod
	def GetClosestDialogToPosition(self, position: Vector3) -> Instance:
		pass

	@abstractmethod
	def GetEmotesMenuOpen(self) -> bool:
		pass

	@abstractmethod
	def GetErrorCode(self) -> ConnectionError:
		pass

	@abstractmethod
	def GetErrorMessage(self) -> str:
		pass

	@abstractmethod
	def GetErrorType(self) -> ConnectionError:
		pass

	@abstractmethod
	def GetGameplayPausedNotificationEnabled(self) -> bool:
		pass

	@abstractmethod
	def GetGuiInset(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetGuiIsVisible(self, guiType: GuiType) -> bool:
		pass

	@abstractmethod
	def GetInspectMenuEnabled(self) -> bool:
		pass

	@abstractmethod
	def GetNotificationTypeList(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetResolutionScale(self) -> int:
		pass

	@abstractmethod
	def GetSafeZoneOffsets(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetUiMessage(self) -> str:
		pass

	@abstractmethod
	def InspectPlayerFromHumanoidDescription(self, humanoidDescription: Instance, name: str) -> None:
		pass

	@abstractmethod
	def InspectPlayerFromUserId(self, userId: int) -> None:
		pass

	@abstractmethod
	def InspectPlayerFromUserIdWithCtx(self, userId: int, ctx: str) -> None:
		pass

	@abstractmethod
	def IsMemoryTrackerEnabled(self) -> bool:
		pass

	@abstractmethod
	def IsTenFootInterface(self) -> bool:
		pass

	@abstractmethod
	def OpenBrowserWindow(self, url: str) -> None:
		pass

	@abstractmethod
	def OpenNativeOverlay(self, title: str, url: str) -> None:
		pass

	@abstractmethod
	def RemoveCenterDialog(self, dialog: Instance) -> None:
		pass

	@abstractmethod
	def RemoveKey(self, key: str) -> None:
		pass

	@abstractmethod
	def RemoveSelectionGroup(self, selectionName: str) -> None:
		pass

	@abstractmethod
	def RemoveSpecialKey(self, key: SpecialKey) -> None:
		pass

	@abstractmethod
	def Select(self, selectionParent: Instance) -> None:
		pass

	@abstractmethod
	def SetEmotesMenuOpen(self, isOpen: bool) -> None:
		pass

	@abstractmethod
	def SetGameplayPausedNotificationEnabled(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetGlobalGuiInset(self, x1: int, y1: int, x2: int, y2: int) -> None:
		pass

	@abstractmethod
	def SetHardwareSafeAreaInsets(self, left: float, top: float, right: float, bottom: float) -> None:
		pass

	@abstractmethod
	def SetInspectMenuEnabled(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetMenuIsOpen(self, open: bool, menuName: str) -> None:
		pass

	@abstractmethod
	def SetSafeZoneOffsets(self, top: float, bottom: float, left: float, right: float) -> None:
		pass

	@abstractmethod
	def SetUiMessage(self, msgType: UiMessageType, uiMessage: str) -> None:
		pass

	@abstractmethod
	def ShowStatsBasedOnInputString(self, input: str) -> bool:
		pass

	@abstractmethod
	def ToggleFullscreen(self) -> None:
		pass

	@abstractmethod
	def ToggleGuiIsVisibleIfAllowed(self, guiType: GuiType) -> None:
		pass

	@abstractmethod
	def GetScreenResolution(self) -> Vector2:
		pass


	pass

class GuidRegistryService(Instance):

	pass

class HapticService(Instance):
	@abstractmethod
	def GetMotor(self, inputType: UserInputType, vibrationMotor: VibrationMotor) -> tuple[Any]:
		pass

	@abstractmethod
	def IsMotorSupported(self, inputType: UserInputType, vibrationMotor: VibrationMotor) -> bool:
		pass

	@abstractmethod
	def IsVibrationSupported(self, inputType: UserInputType) -> bool:
		pass

	@abstractmethod
	def SetMotor(self, inputType: UserInputType, vibrationMotor: VibrationMotor, vibrationValues: tuple[Any]) -> None:
		pass


	pass

class HeightmapImporterService(Instance):
	@abstractmethod
	def CancelImportHeightmap(self) -> None:
		pass

	@abstractmethod
	def IsValidColormap(self, colormapAssetId: Content) -> tuple[Any]:
		pass

	@abstractmethod
	def IsValidHeightmap(self, heightmapAssetId: Content) -> tuple[Any]:
		pass

	@abstractmethod
	def SetImportHeightmapPaused(self, paused: bool) -> None:
		pass

	@abstractmethod
	def GetHeightmapPreviewAsync(self, heightmapAssetId: Content) -> tuple[Any]:
		pass

	@abstractmethod
	def ImportHeightmap(self, region: 'Region3', heightmapAssetId: Content, colormapAssetId: Content, defaultMaterial: Material) -> None:
		pass


	pass

class HiddenSurfaceRemovalAsset(Instance):

	pass

class Highlight(Instance):
	Adornee: Instance
	DepthMode: HighlightDepthMode
	Enabled: bool
	FillColor: Color3
	FillTransparency: float
	LineThickness: int
	OutlineColor: Color3
	OutlineTransparency: float
	ReservedId: ReservedHighlightId

	pass

class Hopper(Instance):

	pass

class HttpRbxApiService(Instance):
	@abstractmethod
	def GetDocumentationUrl(self, partialUrl: str) -> str:
		pass

	@abstractmethod
	def GetAsync(self, apiUrlPath: str, priority: ThrottlingPriority, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def GetAsyncFullUrl(self, apiUrl: str, priority: ThrottlingPriority, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def PostAsync(self, apiUrlPath: str, data: str, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def PostAsyncFullUrl(self, apiUrl: str, data: str, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def RequestAsync(self, requestOptions: dict[Any, Any], priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def RequestLimitedAsync(self, requestOptions: dict[Any, Any], priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType) -> str:
		pass


	pass

class HttpRequest(Instance):
	@abstractmethod
	def Cancel(self) -> None:
		pass

	@abstractmethod
	def Start(self, callback: Callable[..., Any]) -> None:
		pass


	pass

class HttpService(Instance):
	HttpEnabled: bool
	@abstractmethod
	def GenerateGUID(self, wrapInCurlyBraces: bool) -> str:
		pass

	@abstractmethod
	def GetHttpEnabled(self) -> bool:
		pass

	@abstractmethod
	def GetUserAgent(self) -> str:
		pass

	@abstractmethod
	def JSONDecode(self, input: str) -> Any:
		pass

	@abstractmethod
	def JSONEncode(self, input: Any) -> str:
		pass

	@abstractmethod
	def RequestInternal(self, options: dict[Any, Any]) -> Instance:
		pass

	@abstractmethod
	def SetHttpEnabled(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def UrlEncode(self, input: str) -> str:
		pass

	@abstractmethod
	def GetAsync(self, url: str, nocache: bool, headers: Any) -> str:
		pass

	@abstractmethod
	def PostAsync(self, url: str, data: str, content_type: HttpContentType, compress: bool, headers: Any) -> str:
		pass

	@abstractmethod
	def RequestAsync(self, requestOptions: dict[Any, Any]) -> dict[Any, Any]:
		pass


	pass

class Humanoid(Instance):
	AutoJumpEnabled: bool
	AutoRotate: bool
	AutomaticScalingEnabled: bool
	BreakJointsOnDeath: bool
	CameraOffset: Vector3
	CollisionType: HumanoidCollisionType
	DisplayDistanceType: HumanoidDisplayDistanceType
	DisplayName: str
	EvaluateStateMachine: bool
	FloorMaterial: Material
	Health: float
	HealthDisplayDistance: float
	HealthDisplayType: HumanoidHealthDisplayType
	HipHeight: float
	Jump: bool
	JumpHeight: float
	JumpPower: float
	LeftLeg: 'BasePart'
	MaxHealth: float
	MaxSlopeAngle: float
	MoveDirection: Vector3
	NameDisplayDistance: float
	PlatformStand: bool
	RequiresNeck: bool
	RigType: HumanoidRigType
	RightLeg: 'BasePart'
	RootPart: 'BasePart'
	SeatPart: 'BasePart'
	Sit: bool
	TargetPoint: Vector3
	Torso: 'BasePart'
	UseJumpPower: bool
	WalkSpeed: float
	WalkToPart: 'BasePart'
	WalkToPoint: Vector3
	maxHealth: float
	NameOcclusion: NameOcclusion
	@abstractmethod
	def AddAccessory(self, accessory: Instance) -> None:
		pass

	@abstractmethod
	def AddCustomStatus(self, status: str) -> bool:
		pass

	@abstractmethod
	def AddStatus(self, status: 'Status') -> bool:
		pass

	@abstractmethod
	def ApplyDescriptionBlocking(self, humanoidDescription: 'HumanoidDescription') -> None:
		pass

	@abstractmethod
	def BuildRigFromAttachments(self) -> None:
		pass

	@abstractmethod
	def CacheDefaults(self) -> None:
		pass

	@abstractmethod
	def ChangeState(self, state: HumanoidStateType) -> None:
		pass

	@abstractmethod
	def EquipTool(self, tool: Instance) -> None:
		pass

	@abstractmethod
	def GetAccessories(self) -> list[Any]:
		pass

	@abstractmethod
	def GetAccessoryHandleScale(self, instance: Instance, partType: BodyPartR15) -> Vector3:
		pass

	@abstractmethod
	def GetAppliedDescription(self) -> 'HumanoidDescription':
		pass

	@abstractmethod
	def GetBodyPartR15(self, part: Instance) -> BodyPartR15:
		pass

	@abstractmethod
	def GetLimb(self, part: Instance) -> Limb:
		pass

	@abstractmethod
	def GetPlayingAnimationTracks(self) -> list[Any]:
		pass

	@abstractmethod
	def GetState(self) -> HumanoidStateType:
		pass

	@abstractmethod
	def GetStateEnabled(self, state: HumanoidStateType) -> bool:
		pass

	@abstractmethod
	def GetStatuses(self) -> list[Any]:
		pass

	@abstractmethod
	def HasCustomStatus(self, status: str) -> bool:
		pass

	@abstractmethod
	def HasStatus(self, status: 'Status') -> bool:
		pass

	@abstractmethod
	def LoadAnimation(self, animation: Animation) -> AnimationTrack:
		pass

	@abstractmethod
	def Move(self, moveDirection: Vector3, relativeToCamera: bool) -> None:
		pass

	@abstractmethod
	def MoveTo(self, location: Vector3, part: Instance) -> None:
		pass

	@abstractmethod
	def RemoveAccessories(self) -> None:
		pass

	@abstractmethod
	def RemoveCustomStatus(self, status: str) -> bool:
		pass

	@abstractmethod
	def RemoveStatus(self, status: 'Status') -> bool:
		pass

	@abstractmethod
	def ReplaceBodyPartR15(self, bodyPart: BodyPartR15, part: 'BasePart') -> bool:
		pass

	@abstractmethod
	def SetClickToWalkEnabled(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetStateEnabled(self, state: HumanoidStateType, enabled: bool) -> None:
		pass

	@abstractmethod
	def TakeDamage(self, amount: float) -> None:
		pass

	@abstractmethod
	def UnequipTools(self) -> None:
		pass

	@abstractmethod
	def loadAnimation(self, animation: Animation) -> AnimationTrack:
		pass

	@abstractmethod
	def takeDamage(self, amount: float) -> None:
		pass

	@abstractmethod
	def ApplyDescription(self, humanoidDescription: 'HumanoidDescription', assetTypeVerification: AssetTypeVerification) -> None:
		pass

	@abstractmethod
	def ApplyDescriptionClientServer(self, humanoidDescription: 'HumanoidDescription') -> None:
		pass

	@abstractmethod
	def ApplyDescriptionReset(self, humanoidDescription: 'HumanoidDescription', assetTypeVerification: AssetTypeVerification) -> None:
		pass

	@abstractmethod
	def PlayEmote(self, emoteName: str) -> bool:
		pass

	@abstractmethod
	def PlayEmoteAndGetAnimTrackById(self, emoteId: int) -> tuple[Any]:
		pass


	pass

class HumanoidDescription(Instance):
	AccessoryBlob: str
	BackAccessory: str
	BodyTypeScale: float
	ClimbAnimation: int
	DepthScale: float
	Face: int
	FaceAccessory: str
	FallAnimation: int
	FrontAccessory: str
	GraphicTShirt: int
	HairAccessory: str
	HatAccessory: str
	Head: int
	HeadColor: Color3
	HeadScale: float
	HeightScale: float
	IdleAnimation: int
	JumpAnimation: int
	LeftArm: int
	LeftArmColor: Color3
	LeftLeg: int
	LeftLegColor: Color3
	MoodAnimation: int
	NeckAccessory: str
	NumberEmotesLoaded: int
	Pants: int
	ProportionScale: float
	RightArm: int
	RightArmColor: Color3
	RightLeg: int
	RightLegColor: Color3
	RunAnimation: int
	Shirt: int
	ShouldersAccessory: str
	SwimAnimation: int
	Torso: int
	TorsoColor: Color3
	WaistAccessory: str
	WalkAnimation: int
	WidthScale: float
	@abstractmethod
	def AddEmote(self, name: str, assetId: int) -> None:
		pass

	@abstractmethod
	def GetAccessories(self, includeRigidAccessories: bool) -> list[Any]:
		pass

	@abstractmethod
	def GetEmotes(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetEquippedEmotes(self) -> list[Any]:
		pass

	@abstractmethod
	def RemoveEmote(self, name: str) -> None:
		pass

	@abstractmethod
	def SetAccessories(self, accessories: list[Any], includeRigidAccessories: bool) -> None:
		pass

	@abstractmethod
	def SetEmotes(self, emotes: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SetEquippedEmotes(self, equippedEmotes: list[Any]) -> None:
		pass


	pass

class IKControl(Instance):
	AlignmentOffset: CFrame
	ChainRoot: Instance
	Enabled: bool
	EndEffector: Instance
	Offset: CFrame
	Pole: Instance
	Priority: int
	Target: Instance
	Type: IKControlType
	Weight: float

	pass

class ILegacyStudioBridge(Instance):

	pass

class LegacyStudioBridge(ILegacyStudioBridge):

	pass

class IXPService(Instance):
	@abstractmethod
	def ClearUserLayers(self) -> None:
		pass

	@abstractmethod
	def GetBrowserTrackerLayerLoadingStatus(self) -> IXPLoadingStatus:
		pass

	@abstractmethod
	def GetBrowserTrackerLayerVariables(self, layerName: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetBrowserTrackerStatusForLayer(self, layerName: str) -> IXPLoadingStatus| None:
		pass

	@abstractmethod
	def GetRegisteredUserLayersToStatus(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetUserLayerLoadingStatus(self) -> IXPLoadingStatus:
		pass

	@abstractmethod
	def GetUserLayerVariables(self, layerName: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetUserStatusForLayer(self, layerName: str) -> IXPLoadingStatus| None:
		pass

	@abstractmethod
	def InitializeUserLayers(self, userId: int) -> None:
		pass

	@abstractmethod
	def LogBrowserTrackerLayerExposure(self, layerName: str) -> None:
		pass

	@abstractmethod
	def LogUserLayerExposure(self, layerName: str) -> None:
		pass

	@abstractmethod
	def RegisterUserLayers(self, userLayers: Any) -> None:
		pass


	pass

class ImporterBaseSettings(Instance):
	Id: str
	ImportName: str
	ShouldImport: bool
	@abstractmethod
	def GetStatuses(self) -> dict[Any, Any]:
		pass


	pass

class ImporterAnimationSettings(ImporterBaseSettings):

	pass

class ImporterFacsSettings(ImporterBaseSettings):

	pass

class ImporterGroupSettings(ImporterBaseSettings):
	Anchored: bool
	ImportAsModelAsset: bool
	InsertInWorkspace: bool

	pass

class ImporterJointSettings(ImporterBaseSettings):

	pass

class ImporterMaterialSettings(ImporterBaseSettings):
	DiffuseFilePath: str
	IsPbr: bool
	MetalnessFilePath: str
	NormalFilePath: str
	RoughnessFilePath: str

	pass

class ImporterMeshSettings(ImporterBaseSettings):
	Anchored: bool
	CageManifold: bool
	CageMeshIntersectedPreview: bool
	CageMeshNotIntersected: bool
	CageNoOverlappingVertices: bool
	CageNonManifoldPreview: bool
	CageOverlappingVerticesPreview: bool
	CageUVMatched: bool
	CageUVMisMatchedPreview: bool
	Dimensions: Vector3
	DoubleSided: bool
	IgnoreVertexColors: bool
	IrrelevantCageModifiedPreview: bool
	MeshHoleDetectedPreview: bool
	MeshNoHoleDetected: bool
	NoIrrelevantCageModified: bool
	NoOuterCageFarExtendedFromMesh: bool
	OuterCageFarExtendedFromMeshPreview: bool
	PolygonCount: float
	UseImportedPivot: bool

	pass

class ImporterRootSettings(ImporterBaseSettings):
	Anchored: bool
	FileDimensions: Vector3
	ImportAsModelAsset: bool
	InsertInWorkspace: bool
	InsertWithScenePosition: bool
	InvertNegativeFaces: bool
	MergeMeshes: bool
	PolygonCount: float
	ScaleUnit: MeshScaleUnit
	UseSceneOriginAsPivot: bool
	WorldForward: NormalId
	WorldUp: NormalId
	RigType: RigType

	pass

class IncrementalPatchBuilder(Instance):
	HighCompression: bool
	ZstdCompression: bool

	pass

class InputObject(Instance):
	Delta: Vector3
	Position: Vector3
	KeyCode: KeyCode
	UserInputState: UserInputState
	UserInputType: UserInputType
	@abstractmethod
	def IsModifierKeyDown(self, modifierKey: ModifierKey) -> bool:
		pass


	pass

class InsertService(Instance):
	AllowClientInsertModels: bool
	AllowInsertFreeModels: bool
	@abstractmethod
	def ApproveAssetId(self, assetId: int) -> None:
		pass

	@abstractmethod
	def ApproveAssetVersionId(self, assetVersionId: int) -> None:
		pass

	@abstractmethod
	def Insert(self, instance: Instance) -> None:
		pass

	@abstractmethod
	def LoadLocalAsset(self, assetPath: str) -> Instance:
		pass

	@abstractmethod
	def LoadPackageAsset(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def CreateMeshPartAsync(self, meshId: Content, collisionFidelity: CollisionFidelity, renderFidelity: RenderFidelity) -> 'MeshPart':
		pass

	@abstractmethod
	def GetBaseCategories(self) -> list[Any]:
		pass

	@abstractmethod
	def GetBaseSets(self) -> list[Any]:
		pass

	@abstractmethod
	def GetCollection(self, categoryId: int) -> list[Any]:
		pass

	@abstractmethod
	def GetFreeDecals(self, searchText: str, pageNum: int) -> list[Any]:
		pass

	@abstractmethod
	def GetFreeModels(self, searchText: str, pageNum: int) -> list[Any]:
		pass

	@abstractmethod
	def GetLatestAssetVersionAsync(self, assetId: int) -> int:
		pass

	@abstractmethod
	def GetUserCategories(self, userId: int) -> list[Any]:
		pass

	@abstractmethod
	def GetUserSets(self, userId: int) -> list[Any]:
		pass

	@abstractmethod
	def LoadAsset(self, assetId: int) -> Instance:
		pass

	@abstractmethod
	def LoadAssetVersion(self, assetVersionId: int) -> Instance:
		pass

	@abstractmethod
	def LoadPackageAssetAsync(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def loadAsset(self, assetId: int) -> Instance:
		pass


	pass

class JointInstance(Instance):
	Active: bool
	C0: CFrame
	C1: CFrame
	Enabled: bool
	Part0: 'BasePart'
	Part1: 'BasePart'
	part1: 'BasePart'

	pass

class DynamicRotate(JointInstance):
	BaseAngle: float

	pass

class RotateP(DynamicRotate):

	pass

class RotateV(DynamicRotate):

	pass

class Glue(JointInstance):
	F0: Vector3
	F1: Vector3
	F2: Vector3
	F3: Vector3

	pass

class ManualSurfaceJointInstance(JointInstance):

	pass

class ManualGlue(ManualSurfaceJointInstance):

	pass

class ManualWeld(ManualSurfaceJointInstance):

	pass

class Motor(JointInstance):
	CurrentAngle: float
	DesiredAngle: float
	MaxVelocity: float
	@abstractmethod
	def SetDesiredAngle(self, value: float) -> None:
		pass


	pass

class Motor6D(Motor):
	ChildName: str
	ParentName: str
	Transform: CFrame

	pass

class Rotate(JointInstance):

	pass

class Snap(JointInstance):

	pass

class VelocityMotor(JointInstance):
	CurrentAngle: float
	DesiredAngle: float
	MaxVelocity: float
	Hole: Hole

	pass

class Weld(JointInstance):

	pass

class JointsService(Instance):
	@abstractmethod
	def ClearJoinAfterMoveJoints(self) -> None:
		pass

	@abstractmethod
	def CreateJoinAfterMoveJoints(self) -> None:
		pass

	@abstractmethod
	def SetJoinAfterMoveInstance(self, joinInstance: Instance) -> None:
		pass

	@abstractmethod
	def SetJoinAfterMoveTarget(self, joinTarget: Instance) -> None:
		pass

	@abstractmethod
	def ShowPermissibleJoints(self) -> None:
		pass


	pass

class KeyboardService(Instance):

	pass

class Keyframe(Instance):
	Time: float
	@abstractmethod
	def AddMarker(self, marker: Instance) -> None:
		pass

	@abstractmethod
	def AddPose(self, pose: Instance) -> None:
		pass

	@abstractmethod
	def GetMarkers(self) -> list[Instance]:
		pass

	@abstractmethod
	def GetPoses(self) -> list[Instance]:
		pass

	@abstractmethod
	def RemoveMarker(self, marker: Instance) -> None:
		pass

	@abstractmethod
	def RemovePose(self, pose: Instance) -> None:
		pass


	pass

class KeyframeMarker(Instance):
	Value: str

	pass

class KeyframeSequenceProvider(Instance):
	@abstractmethod
	def GetKeyframeSequence(self, assetId: Content) -> Instance:
		pass

	@abstractmethod
	def GetKeyframeSequenceById(self, assetId: int, useCache: bool) -> Instance:
		pass

	@abstractmethod
	def GetMemStats(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def RegisterActiveKeyframeSequence(self, keyframeSequence: Instance) -> Content:
		pass

	@abstractmethod
	def RegisterKeyframeSequence(self, keyframeSequence: Instance) -> Content:
		pass

	@abstractmethod
	def GetAnimations(self, userId: int) -> Instance:
		pass

	@abstractmethod
	def GetKeyframeSequenceAsync(self, assetId: Content) -> Instance:
		pass


	pass

class LSPFileSyncService(Instance):

	pass

class LanguageService(Instance):

	pass

class Light(Instance):
	Brightness: float
	Color: Color3
	Enabled: bool
	Shadows: bool

	pass

class PointLight(Light):
	Range: float

	pass

class SpotLight(Light):
	Angle: float
	Face: NormalId
	Range: float

	pass

class SurfaceLight(Light):
	Angle: float
	Face: NormalId
	Range: float

	pass

class Lighting(Instance):
	Ambient: Color3
	Brightness: float
	ClockTime: float
	ColorShiftBottom: Color3
	ColorShiftTop: Color3
	EnvironmentDiffuseScale: float
	EnvironmentSpecularScale: float
	ExposureCompensation: float
	FogColor: Color3
	FogEnd: float
	FogStart: float
	GeographicLatitude: float
	GlobalShadows: bool
	OutdoorAmbient: Color3
	Outlines: bool
	ShadowColor: Color3
	ShadowSoftness: float
	TempUseNewSkyRemovalBehaviour: bool
	TimeOfDay: str
	Technology: Technology
	@abstractmethod
	def GetMinutesAfterMidnight(self) -> float:
		pass

	@abstractmethod
	def GetMoonDirection(self) -> Vector3:
		pass

	@abstractmethod
	def GetMoonPhase(self) -> float:
		pass

	@abstractmethod
	def GetSunDirection(self) -> Vector3:
		pass

	@abstractmethod
	def SetMinutesAfterMidnight(self, minutes: float) -> None:
		pass

	@abstractmethod
	def getMinutesAfterMidnight(self) -> float:
		pass

	@abstractmethod
	def setMinutesAfterMidnight(self, minutes: float) -> None:
		pass


	pass

class LocalStorageService(Instance):
	@abstractmethod
	def Flush(self) -> None:
		pass

	@abstractmethod
	def GetItem(self, key: str) -> str:
		pass

	@abstractmethod
	def SetItem(self, key: str, value: str) -> None:
		pass

	@abstractmethod
	def WhenLoaded(self, callback: Callable[..., Any]) -> None:
		pass


	pass

class AppStorageService(LocalStorageService):

	pass

class UserStorageService(LocalStorageService):

	pass

class LocalizationService(Instance):
	ForcePlayModeGameLocaleId: str
	ForcePlayModeRobloxLocaleId: str
	IsTextScraperRunning: bool
	RobloxForcePlayModeGameLocaleId: str
	RobloxForcePlayModeRobloxLocaleId: str
	RobloxLocaleId: str
	SystemLocaleId: str
	@abstractmethod
	def GetCorescriptLocalizations(self) -> list[Instance]:
		pass

	@abstractmethod
	def GetTableEntries(self, instance: Instance) -> list[Any]:
		pass

	@abstractmethod
	def GetTranslatorForPlayer(self, player: Instance) -> Instance:
		pass

	@abstractmethod
	def SetRobloxLocaleId(self, locale: str) -> None:
		pass

	@abstractmethod
	def StartTextScraper(self) -> None:
		pass

	@abstractmethod
	def StopTextScraper(self) -> None:
		pass

	@abstractmethod
	def GetCountryRegionForPlayerAsync(self, player: Instance) -> str:
		pass

	@abstractmethod
	def GetTranslatorForLocaleAsync(self, locale: str) -> Instance:
		pass

	@abstractmethod
	def GetTranslatorForPlayerAsync(self, player: Instance) -> Instance:
		pass

	@abstractmethod
	def PromptDownloadGameTableToCSV(self, table: Instance) -> None:
		pass

	@abstractmethod
	def PromptExportToCSVs(self) -> None:
		pass

	@abstractmethod
	def PromptImportFromCSVs(self) -> None:
		pass

	@abstractmethod
	def PromptUploadCSVToGameTable(self) -> Instance:
		pass


	pass

class LocalizationTable(Instance):
	DevelopmentLanguage: str
	Root: Instance
	SourceLocaleId: str
	@abstractmethod
	def GetContents(self) -> str:
		pass

	@abstractmethod
	def GetEntries(self) -> list[Any]:
		pass

	@abstractmethod
	def GetString(self, targetLocaleId: str, key: str) -> str:
		pass

	@abstractmethod
	def GetTranslator(self, localeId: str) -> Instance:
		pass

	@abstractmethod
	def RemoveEntry(self, key: str, source: str, context: str) -> None:
		pass

	@abstractmethod
	def RemoveEntryValue(self, key: str, source: str, context: str, localeId: str) -> None:
		pass

	@abstractmethod
	def RemoveKey(self, key: str) -> None:
		pass

	@abstractmethod
	def RemoveTargetLocale(self, localeId: str) -> None:
		pass

	@abstractmethod
	def SetContents(self, contents: str) -> None:
		pass

	@abstractmethod
	def SetEntries(self, entries: Any) -> None:
		pass

	@abstractmethod
	def SetEntry(self, key: str, targetLocaleId: str, text: str) -> None:
		pass

	@abstractmethod
	def SetEntryContext(self, key: str, source: str, context: str, newContext: str) -> None:
		pass

	@abstractmethod
	def SetEntryExample(self, key: str, source: str, context: str, example: str) -> None:
		pass

	@abstractmethod
	def SetEntryKey(self, key: str, source: str, context: str, newKey: str) -> None:
		pass

	@abstractmethod
	def SetEntrySource(self, key: str, source: str, context: str, newSource: str) -> None:
		pass

	@abstractmethod
	def SetEntryValue(self, key: str, source: str, context: str, localeId: str, text: str) -> None:
		pass

	@abstractmethod
	def SetIsExemptFromUGCAnalytics(self, value: bool) -> None:
		pass


	pass

class CloudLocalizationTable(LocalizationTable):

	pass

class LodDataEntity(Instance):
	EntityLodEnabled: bool

	pass

class LodDataService(Instance):

	pass

class LogService(Instance):
	@abstractmethod
	def ExecuteScript(self, source: str) -> None:
		pass

	@abstractmethod
	def GetHttpResultHistory(self) -> list[Any]:
		pass

	@abstractmethod
	def GetLogHistory(self) -> list[Any]:
		pass

	@abstractmethod
	def RequestHttpResultApproved(self) -> None:
		pass

	@abstractmethod
	def RequestServerHttpResult(self) -> None:
		pass

	@abstractmethod
	def RequestServerOutput(self) -> None:
		pass


	pass

class LoginService(Instance):
	@abstractmethod
	def Logout(self) -> None:
		pass

	@abstractmethod
	def PromptLogin(self) -> None:
		pass


	pass

class LuaSettings(Instance):

	pass

class LuaSourceContainer(Instance):
	CurrentEditor: Instance

	pass

class BaseScript(LuaSourceContainer):
	Disabled: bool
	Enabled: bool
	LinkedSource: Content
	RunContext: RunContext

	pass

class CoreScript(BaseScript):

	pass

class Script(BaseScript):
	Source: ProtectedString
	@abstractmethod
	def GetHash(self) -> str:
		pass


	pass

class LocalScript(Script):

	pass

class ModuleScript(LuaSourceContainer):
	LinkedSource: Content
	Source: ProtectedString

	pass

class LuaWebService(Instance):

	pass

class LuauScriptAnalyzerService(Instance):

	pass

class MarkerCurve(Instance):
	Length: int
	@abstractmethod
	def GetMarkerAtIndex(self, index: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetMarkers(self) -> list[Any]:
		pass

	@abstractmethod
	def InsertMarkerAtTime(self, time: float, marker: str) -> list[Any]:
		pass

	@abstractmethod
	def RemoveMarkerAtIndex(self, startingIndex: int, count: int) -> int:
		pass


	pass

class MarketplaceService(Instance):
	@abstractmethod
	def PlayerCanMakePurchases(self, player: Instance) -> bool:
		pass

	@abstractmethod
	def PromptBundlePurchase(self, player: Instance, bundleId: int) -> None:
		pass

	@abstractmethod
	def PromptGamePassPurchase(self, player: Instance, gamePassId: int) -> None:
		pass

	@abstractmethod
	def PromptNativePurchase(self, player: Instance, productId: str) -> None:
		pass

	@abstractmethod
	def PromptNativePurchaseWithLocalPlayer(self, productId: str) -> None:
		pass

	@abstractmethod
	def PromptPremiumPurchase(self, player: Instance) -> None:
		pass

	@abstractmethod
	def PromptProductPurchase(self, player: Instance, productId: int, equipIfPurchased: bool, currencyType: CurrencyType) -> None:
		pass

	@abstractmethod
	def PromptPurchase(self, player: Instance, assetId: int, equipIfPurchased: bool, currencyType: CurrencyType) -> None:
		pass

	@abstractmethod
	def PromptRobloxPurchase(self, assetId: int, equipIfPurchased: bool) -> None:
		pass

	@abstractmethod
	def PromptSubscriptionCancellation(self, player: Instance, subscriptionId: int) -> None:
		pass

	@abstractmethod
	def PromptSubscriptionPurchase(self, player: Instance, subscriptionId: int) -> None:
		pass

	@abstractmethod
	def PromptThirdPartyPurchase(self, player: Instance, productId: str) -> None:
		pass

	@abstractmethod
	def ReportAssetSale(self, assetId: str, robuxAmount: int) -> None:
		pass

	@abstractmethod
	def ReportRobuxUpsellStarted(self) -> None:
		pass

	@abstractmethod
	def SignalAssetTypePurchased(self, player: Instance, assetType: AssetType) -> None:
		pass

	@abstractmethod
	def SignalClientPurchaseSuccess(self, ticket: str, playerId: int, productId: int) -> None:
		pass

	@abstractmethod
	def SignalMockPurchasePremium(self) -> None:
		pass

	@abstractmethod
	def SignalPromptBundlePurchaseFinished(self, player: Instance, bundleId: int, success: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptGamePassPurchaseFinished(self, player: Instance, gamePassId: int, success: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptPremiumPurchaseFinished(self, didTryPurchasing: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptProductPurchaseFinished(self, userId: int, productId: int, success: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptPurchaseFinished(self, player: Instance, assetId: int, success: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptSubscriptionCancellationFinished(self, player: Instance, subscriptionId: int, wasCanceled: bool) -> None:
		pass

	@abstractmethod
	def SignalPromptSubscriptionPurchaseFinished(self, player: Instance, subscriptionId: int, wasPurchased: bool) -> None:
		pass

	@abstractmethod
	def SignalServerLuaDialogClosed(self, value: bool) -> None:
		pass

	@abstractmethod
	def GetDeveloperProductsAsync(self) -> Instance:
		pass

	@abstractmethod
	def GetProductInfo(self, assetId: int, infoType: InfoType) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetRobuxBalance(self) -> int:
		pass

	@abstractmethod
	def IsPlayerSubscribed(self, player: Instance, subscriptionId: int) -> bool:
		pass

	@abstractmethod
	def PerformPurchase(self, infoType: InfoType, productId: int, expectedPrice: int, requestId: str, isRobloxPurchase: bool) -> dict[Any, Any]:
		pass

	@abstractmethod
	def PlayerOwnsAsset(self, player: Instance, assetId: int) -> bool:
		pass

	@abstractmethod
	def PlayerOwnsBundle(self, player: 'Player', bundleId: int) -> bool:
		pass

	@abstractmethod
	def UserOwnsGamePassAsync(self, userId: int, gamePassId: int) -> bool:
		pass


	pass

class MaterialService(Instance):
	AsphaltName: str
	BasaltName: str
	BrickName: str
	CobblestoneName: str
	ConcreteName: str
	CorrodedMetalName: str
	CrackedLavaName: str
	DiamondPlateName: str
	FabricName: str
	FoilName: str
	GlacierName: str
	GraniteName: str
	GrassName: str
	GroundName: str
	IceName: str
	LeafyGrassName: str
	LimestoneName: str
	MarbleName: str
	MetalName: str
	MudName: str
	PavementName: str
	PebbleName: str
	PlasticName: str
	RockName: str
	SaltName: str
	SandName: str
	SandstoneName: str
	SlateName: str
	SmoothPlasticName: str
	SnowName: str
	Use2022Materials: bool
	WoodName: str
	WoodPlanksName: str
	@abstractmethod
	def GetBaseMaterialOverride(self, material: Material) -> str:
		pass

	@abstractmethod
	def GetMaterialOverrideChanged(self, material: Material) -> 'RBXScriptSignal':
		pass

	@abstractmethod
	def GetMaterialVariant(self, material: Material, name: str) -> 'MaterialVariant':
		pass

	@abstractmethod
	def GetOverrideStatus(self, material: Material) -> PropertyStatus:
		pass

	@abstractmethod
	def SetBaseMaterialOverride(self, material: Material, name: str) -> None:
		pass


	pass

class MaterialVariant(Instance):
	BaseMaterial: Material
	ColorMap: Content
	CustomPhysicalProperties: PhysicalProperties
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	StudsPerTile: float
	MaterialPattern: MaterialPattern

	pass

class MemStorageConnection(Instance):
	@abstractmethod
	def Disconnect(self) -> None:
		pass


	pass

class MemStorageService(Instance):
	@abstractmethod
	def Bind(self, key: str, callback: Callable[..., Any]) -> MemStorageConnection:
		pass

	@abstractmethod
	def BindAndFire(self, key: str, callback: Callable[..., Any]) -> MemStorageConnection:
		pass

	@abstractmethod
	def Call(self, key: str, input: Any) -> Any:
		pass

	@abstractmethod
	def Fire(self, key: str, value: str) -> None:
		pass

	@abstractmethod
	def GetItem(self, key: str, defaultValue: str) -> str:
		pass

	@abstractmethod
	def HasItem(self, key: str) -> bool:
		pass

	@abstractmethod
	def RemoveItem(self, key: str) -> bool:
		pass

	@abstractmethod
	def SetItem(self, key: str, value: str) -> None:
		pass


	pass

class MemoryStoreQueue(Instance):
	@abstractmethod
	def AddAsync(self, value: Any, expiration: int, priority: float) -> None:
		pass

	@abstractmethod
	def ReadAsync(self, count: int, allOrNothing: bool, waitTimeout: float) -> tuple[Any]:
		pass

	@abstractmethod
	def RemoveAsync(self, id: str) -> None:
		pass


	pass

class MemoryStoreService(Instance):
	@abstractmethod
	def GetQueue(self, name: str, invisibilityTimeout: int) -> MemoryStoreQueue:
		pass

	@abstractmethod
	def GetSortedMap(self, name: str) -> 'MemoryStoreSortedMap':
		pass


	pass

class MemoryStoreSortedMap(Instance):
	@abstractmethod
	def GetAsync(self, key: str) -> Any:
		pass

	@abstractmethod
	def GetRangeAsync(self, direction: SortDirection, count: int, exclusiveLowerBound: str, exclusiveUpperBound: str) -> list[Any]:
		pass

	@abstractmethod
	def RemoveAsync(self, key: str) -> None:
		pass

	@abstractmethod
	def SetAsync(self, key: str, value: Any, expiration: int) -> bool:
		pass

	@abstractmethod
	def UpdateAsync(self, key: str, transformFunction: Callable[..., Any], expiration: int) -> Any:
		pass


	pass

class Message(Instance):
	Text: str

	pass

class Hint(Message):

	pass

class MessageBusConnection(Instance):
	@abstractmethod
	def Disconnect(self) -> None:
		pass


	pass

class MessageBusService(Instance):
	@abstractmethod
	def Call(self, key: str, input: Any) -> Any:
		pass

	@abstractmethod
	def GetLast(self, mid: str) -> Any:
		pass

	@abstractmethod
	def GetMessageId(self, domainName: str, messageName: str) -> str:
		pass

	@abstractmethod
	def GetProtocolMethodRequestMessageId(self, protocolName: str, methodName: str) -> str:
		pass

	@abstractmethod
	def GetProtocolMethodResponseMessageId(self, protocolName: str, methodName: str) -> str:
		pass

	@abstractmethod
	def Publish(self, mid: str, params: Any) -> None:
		pass

	@abstractmethod
	def PublishProtocolMethodRequest(self, protocolName: str, methodName: str, message: Any, customTelemetryData: Any) -> None:
		pass

	@abstractmethod
	def PublishProtocolMethodResponse(self, protocolName: str, methodName: str, message: Any, responseCode: int, customTelemetryData: Any) -> None:
		pass

	@abstractmethod
	def Subscribe(self, mid: str, callback: Callable[..., Any], once: bool, sticky: bool) -> Instance:
		pass

	@abstractmethod
	def SubscribeToProtocolMethodRequest(self, protocolName: str, methodName: str, callback: Callable[..., Any], once: bool, sticky: bool) -> Instance:
		pass

	@abstractmethod
	def SubscribeToProtocolMethodResponse(self, protocolName: str, methodName: str, callback: Callable[..., Any], once: bool, sticky: bool) -> Instance:
		pass


	pass

class MessagingService(Instance):
	@abstractmethod
	def PublishAsync(self, topic: str, message: Any) -> None:
		pass

	@abstractmethod
	def SubscribeAsync(self, topic: str, callback: Callable[..., Any]) -> 'RBXScriptConnection':
		pass


	pass

class MetaBreakpoint(Instance):
	Condition: str
	ContinueExecution: bool
	Enabled: bool
	Id: int
	IsLogpoint: bool
	Line: int
	LogMessage: str
	Script: str
	Valid: bool
	@abstractmethod
	def GetContextBreakpoints(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def RemoveMetaBreakpoint(self, status: Callable[..., Any]) -> int: # Overloading + Overriding
		pass

	@abstractmethod
	def SetChildBreakpointEnabledByScriptAndContext(self, script: str, contextGST: int, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetContextEnabled(self, context: int, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetContinueExecution(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetEnabled(self, enabled: bool) -> None:
		pass

	@abstractmethod
	def SetLine(self, line: int, status: Callable[..., Any]) -> int:
		pass


	pass

class MetaBreakpointContext(Instance):

	pass

class MetaBreakpointManager(Instance):
	@abstractmethod
	def AddBreakpoint(self, script: Instance, line: int, condition: Instance) -> Instance:
		pass

	@abstractmethod
	def GetBreakpointById(self, metaBreakpointId: int) -> MetaBreakpoint:
		pass

	@abstractmethod
	def RemoveBreakpointById(self, metaBreakpointId: int) -> None:
		pass


	pass

class Mouse(Instance):
	Hit: CFrame
	Icon: Content
	Origin: CFrame
	Target: 'BasePart'
	TargetFilter: Instance
	TargetSurface: NormalId
	UnitRay: Ray
	ViewSizeX: int
	ViewSizeY: int
	X: int
	Y: int
	hit: CFrame
	target: 'BasePart'

	pass

class PlayerMouse(Mouse):

	pass

class PluginMouse(Mouse):

	pass

class MouseService(Instance):

	pass

class MultipleDocumentInterfaceInstance(Instance):
	FocusedDataModelSession: Instance

	pass

class NetworkMarker(Instance):

	pass

class NetworkPeer(Instance):
	@abstractmethod
	def SetOutgoingKBPSLimit(self, limit: int) -> None:
		pass


	pass

class NetworkClient(NetworkPeer):

	pass

class NetworkServer(NetworkPeer):
	@abstractmethod
	def EncryptStringForPlayerId(self, toEncrypt: str, playerId: int) -> str:
		pass


	pass

class NetworkReplicator(Instance):
	@abstractmethod
	def GetPlayer(self) -> Instance:
		pass


	pass

class ClientReplicator(NetworkReplicator):
	@abstractmethod
	def RequestRCCProfilerData(self, frameRate: int, timeFrame: int) -> None:
		pass

	@abstractmethod
	def RequestServerScriptProfiling(self, start: bool) -> None:
		pass

	@abstractmethod
	def RequestServerStats(self, request: bool) -> None:
		pass


	pass

class ServerReplicator(NetworkReplicator):

	pass

class NetworkSettings(Instance):
	EmulatedTotalMemoryInMB: int
	FreeMemoryMBytes: float
	HttpProxyEnabled: bool
	HttpProxyURL: str
	IncomingReplicationLag: float
	PrintJoinSizeBreakdown: bool
	PrintPhysicsErrors: bool
	PrintStreamInstanceQuota: bool
	RandomizeJoinInstanceOrder: bool
	RenderStreamedRegions: bool
	ShowActiveAnimationAsset: bool

	pass

class NoCollisionConstraint(Instance):
	Enabled: bool
	Part0: 'BasePart'
	Part1: 'BasePart'

	pass

class NotificationService(Instance):
	IsConnected: bool
	IsLuaChatEnabled: bool
	IsLuaGameDetailsEnabled: bool
	SelectedTheme: str
	@abstractmethod
	def ActionEnabled(self, actionType: AppShellActionType) -> None:
		pass

	@abstractmethod
	def ActionTaken(self, actionType: AppShellActionType) -> None:
		pass

	@abstractmethod
	def CancelAllNotification(self, userId: int) -> None:
		pass

	@abstractmethod
	def CancelNotification(self, userId: int, alertId: int) -> None:
		pass

	@abstractmethod
	def ScheduleNotification(self, userId: int, alertId: int, alertMsg: str, minutesToFire: int) -> None:
		pass

	@abstractmethod
	def SwitchedToAppShellFeature(self, appShellFeature: AppShellFeature) -> None:
		pass

	@abstractmethod
	def GetScheduledNotifications(self, userId: int) -> list[Any]:
		pass


	pass

class PVInstance(Instance):
	OriginOrientation: Vector3
	OriginPosition: Vector3
	PivotOffsetOrientation: Vector3
	PivotOffsetPosition: Vector3
	@abstractmethod
	def GetPivot(self) -> CFrame:
		pass

	@abstractmethod
	def PivotTo(self, targetCFrame: CFrame) -> None:
		pass


	pass

class BasePart(PVInstance):
	Anchored: bool
	AssemblyAngularVelocity: Vector3
	AssemblyCenterOfMass: Vector3
	AssemblyLinearVelocity: Vector3
	AssemblyMass: float
	AssemblyRootPart: 'BasePart'
	BackParamA: float
	BackParamB: float
	BackSurface: SurfaceType
	BackSurfaceInput: InputType
	BottomParamA: float
	BottomParamB: float
	BottomSurface: SurfaceType
	BottomSurfaceInput: InputType
	CanCollide: bool
	CanQuery: bool
	CanTouch: bool
	CastShadow: bool
	CenterOfMass: Vector3
	CollisionGroup: str
	CollisionGroupId: int
	Color: Color3
	CurrentPhysicalProperties: PhysicalProperties
	CustomPhysicalProperties: PhysicalProperties
	Elasticity: float
	Friction: float
	FrontParamA: float
	FrontParamB: float
	FrontSurface: SurfaceType
	FrontSurfaceInput: InputType
	LeftParamA: float
	LeftParamB: float
	LeftSurface: SurfaceType
	LeftSurfaceInput: InputType
	LocalTransparencyModifier: float
	Locked: bool
	Mass: float
	Massless: bool
	MaterialVariant: str
	Orientation: Vector3
	PivotOffset: CFrame
	Position: Vector3
	ReceiveAge: float
	Reflectance: float
	ResizeIncrement: int
	ResizeableFaces: Faces
	RightParamA: float
	RightParamB: float
	RightSurface: SurfaceType
	RightSurfaceInput: InputType
	RootPriority: int
	RotVelocity: Vector3
	Rotation: Vector3
	Size: Vector3
	SpecificGravity: float
	TopParamA: float
	TopParamB: float
	TopSurface: SurfaceType
	TopSurfaceInput: InputType
	Transparency: float
	Velocity: Vector3
	brickColor: BrickColor
	BrickColor: BrickColor
	CFrame: CFrame
	Material: Material
	@abstractmethod
	def ApplyAngularImpulse(self, impulse: Vector3) -> None:
		pass

	@abstractmethod
	def ApplyImpulse(self, impulse: Vector3) -> None:
		pass

	@abstractmethod
	def ApplyImpulseAtPosition(self, impulse: Vector3, position: Vector3) -> None:
		pass

	@abstractmethod
	def BreakJoints(self) -> None:
		pass

	@abstractmethod
	def CanCollideWith(self, part: Self) -> bool:
		pass

	@abstractmethod
	def CanSetNetworkOwnership(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetConnectedParts(self, recursive: bool) -> list[Instance]:
		pass

	@abstractmethod
	def GetJoints(self) -> list[Instance]:
		pass

	@abstractmethod
	def GetMass(self) -> float:
		pass

	@abstractmethod
	def GetNetworkOwner(self) -> Instance:
		pass

	@abstractmethod
	def GetNetworkOwnershipAuto(self) -> bool:
		pass

	@abstractmethod
	def GetRenderCFrame(self) -> 'CFrame':
		pass

	@abstractmethod
	def GetRootPart(self) -> Instance:
		pass

	@abstractmethod
	def GetTouchingParts(self) -> list[Instance]:
		pass

	@abstractmethod
	def GetVelocityAtPosition(self, position: Vector3) -> Vector3:
		pass

	@abstractmethod
	def IsGrounded(self) -> bool:
		pass

	@abstractmethod
	def MakeJoints(self) -> None:
		pass

	@abstractmethod
	def Resize(self, normalId: NormalId, deltaAmount: int) -> bool:
		pass

	@abstractmethod
	def SetNetworkOwner(self, playerInstance: 'Player') -> None:
		pass

	@abstractmethod
	def SetNetworkOwnershipAuto(self) -> None:
		pass

	@abstractmethod
	def breakJoints(self) -> None:
		pass

	@abstractmethod
	def getMass(self) -> float:
		pass

	@abstractmethod
	def makeJoints(self) -> None:
		pass

	@abstractmethod
	def resize(self, normalId: NormalId, deltaAmount: int) -> bool:
		pass

	@abstractmethod
	def SubtractAsync(self, parts: list[Instance], collisionfidelity: CollisionFidelity, renderFidelity: RenderFidelity) -> Instance:
		pass

	@abstractmethod
	def UnionAsync(self, parts: list[Instance], collisionfidelity: CollisionFidelity, renderFidelity: RenderFidelity) -> Instance:
		pass


	pass

class CornerWedgePart(BasePart):

	pass

class FormFactorPart(BasePart):
	formFactor: FormFactor
	FormFactor: FormFactor

	pass

class Part(FormFactorPart):
	Shape: PartType

	pass

class FlagStand(Part):
	TeamColor: BrickColor

	pass

class Platform(Part):

	pass

class Seat(Part):
	Disabled: bool
	Occupant: Humanoid
	@abstractmethod
	def Sit(self, humanoid: Instance) -> None:
		pass


	pass

class SkateboardPlatform(Part):
	Controller: SkateboardController
	ControllingHumanoid: Humanoid
	Steer: int
	StickyWheels: bool
	Throttle: int
	@abstractmethod
	def ApplySpecificImpulse(self, impulseWorld: Vector3) -> None:
		pass


	pass

class SpawnLocation(Part):
	AllowTeamChangeOnTouch: bool
	Duration: int
	Enabled: bool
	Neutral: bool
	TeamColor: BrickColor

	pass

class WedgePart(FormFactorPart):

	pass

class Terrain(BasePart):
	Decoration: bool
	IsSmooth: bool
	LastUsedModificationMethod: TerrainAcquisitionMethod
	MaterialColors: BinaryString
	MaxExtents: Region3int16
	WaterColor: Color3
	WaterReflectance: float
	WaterTransparency: float
	WaterWaveSize: float
	WaterWaveSpeed: float
	@abstractmethod
	def AutowedgeCell(self, x: int, y: int, z: int) -> bool:
		pass

	@abstractmethod
	def AutowedgeCells(self, region: Region3int16) -> None:
		pass

	@abstractmethod
	def CellCenterToWorld(self, x: int, y: int, z: int) -> Vector3:
		pass

	@abstractmethod
	def CellCornerToWorld(self, x: int, y: int, z: int) -> Vector3:
		pass

	@abstractmethod
	def Clear(self) -> None:
		pass

	@abstractmethod
	def ConvertToSmooth(self) -> None:
		pass

	@abstractmethod
	def CopyRegion(self, region: Region3int16) -> 'TerrainRegion':
		pass

	@abstractmethod
	def CountCells(self) -> int:
		pass

	@abstractmethod
	def FillBall(self, center: Vector3, radius: float, material: Material) -> None:
		pass

	@abstractmethod
	def FillBlock(self, cframe: CFrame, size: Vector3, material: Material) -> None:
		pass

	@abstractmethod
	def FillCylinder(self, cframe: CFrame, height: float, radius: float, material: Material) -> None:
		pass

	@abstractmethod
	def FillRegion(self, region: 'Region3', resolution: float, material: Material) -> None:
		pass

	@abstractmethod
	def FillWedge(self, cframe: CFrame, size: Vector3, material: Material) -> None:
		pass

	@abstractmethod
	def GetCell(self, x: int, y: int, z: int) -> tuple[Any]:
		pass

	@abstractmethod
	def GetMaterialColor(self, material: Material) -> Color3:
		pass

	@abstractmethod
	def GetWaterCell(self, x: int, y: int, z: int) -> tuple[Any]:
		pass

	@abstractmethod
	def HideTerrainRegion(self) -> None:
		pass

	@abstractmethod
	def PasteRegion(self, region: 'TerrainRegion', corner: 'Vector3int16', pasteEmptyCells: bool) -> None:
		pass

	@abstractmethod
	def ReadVoxels(self, region: 'Region3', resolution: float) -> tuple[Any]:
		pass

	@abstractmethod
	def ReplaceMaterial(self, region: 'Region3', resolution: float, sourceMaterial: Material, targetMaterial: Material) -> None:
		pass

	@abstractmethod
	def SetCell(self, x: int, y: int, z: int, material: CellMaterial, block: CellBlock, orientation: CellOrientation) -> None:
		pass

	@abstractmethod
	def SetCells(self, region: Region3int16, material: CellMaterial, block: CellBlock, orientation: CellOrientation) -> None:
		pass

	@abstractmethod
	def SetMaterialColor(self, material: Material, value: Color3) -> None:
		pass

	@abstractmethod
	def SetTerrainRegion(self, cframe: CFrame, size: Vector3) -> None:
		pass

	@abstractmethod
	def SetWaterCell(self, x: int, y: int, z: int, force: WaterForce, direction: WaterDirection) -> None:
		pass

	@abstractmethod
	def SetWireframeRegion(self, cframe: CFrame, size: Vector3) -> None:
		pass

	@abstractmethod
	def ShowTerrainRegion(self) -> None:
		pass

	@abstractmethod
	def WorldToCell(self, position: Vector3) -> Vector3:
		pass

	@abstractmethod
	def WorldToCellPreferEmpty(self, position: Vector3) -> Vector3:
		pass

	@abstractmethod
	def WorldToCellPreferSolid(self, position: Vector3) -> Vector3:
		pass

	@abstractmethod
	def WriteVoxels(self, region: 'Region3', resolution: float, materials: list[Any], occupancy: list[Any]) -> None:
		pass


	pass

class TriangleMeshPart(BasePart):
	MeshSize: Vector3
	CollisionFidelity: CollisionFidelity

	pass

class MeshPart(TriangleMeshPart):
	DoubleSided: bool
	HasJointOffset: bool
	HasSkinnedMesh: bool
	JointOffset: Vector3
	MeshId: Content
	TextureID: Content
	RenderFidelity: RenderFidelity
	@abstractmethod
	def ApplyMesh(self, meshPart: Instance) -> None:
		pass


	pass

class PartOperation(TriangleMeshPart):
	SmoothingAngle: float
	TriangleCount: int
	UsePartColor: bool
	RenderFidelity: RenderFidelity

	pass

class NegateOperation(PartOperation):

	pass

class UnionOperation(PartOperation):

	pass

class TrussPart(BasePart):
	Style: Style

	pass

class VehicleSeat(BasePart):
	AreHingesDetected: int
	Disabled: bool
	HeadsUpDisplay: bool
	MaxSpeed: float
	Occupant: Humanoid
	Steer: int
	SteerFloat: float
	Throttle: int
	ThrottleFloat: float
	Torque: float
	TurnSpeed: float
	@abstractmethod
	def Sit(self, humanoid: Instance) -> None:
		pass


	pass

class Model(PVInstance):
	LevelOfDetail: ModelLevelOfDetail
	PrimaryPart: BasePart
	WorldPivotOrientation: Vector3
	WorldPivotPosition: Vector3
	WorldPivot: CFrame
	ModelStreamingMode: ModelStreamingMode
	@abstractmethod
	def BreakJoints(self) -> None:
		pass

	@abstractmethod
	def GetBoundingBox(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetExtentsSize(self) -> Vector3:
		pass

	@abstractmethod
	def GetModelCFrame(self) -> CFrame:
		pass

	@abstractmethod
	def GetModelSize(self) -> Vector3:
		pass

	@abstractmethod
	def GetPrimaryPartCFrame(self) -> CFrame:
		pass

	@abstractmethod
	def MakeJoints(self) -> None:
		pass

	@abstractmethod
	def MoveTo(self, position: Vector3) -> None:
		pass

	@abstractmethod
	def ResetOrientationToIdentity(self) -> None:
		pass

	@abstractmethod
	def SetIdentityOrientation(self) -> None:
		pass

	@abstractmethod
	def SetPrimaryPartCFrame(self, cframe: CFrame) -> None:
		pass

	@abstractmethod
	def TranslateBy(self, delta: Vector3) -> None:
		pass

	@abstractmethod
	def breakJoints(self) -> None:
		pass

	@abstractmethod
	def makeJoints(self) -> None:
		pass

	@abstractmethod
	def move(self, location: Vector3) -> None:
		pass

	@abstractmethod
	def moveTo(self, location: Vector3) -> None:
		pass


	pass

class Actor(Model):

	pass

class Status(Model):

	pass

class WorldRoot(Model):
	@abstractmethod
	def ArePartsTouchingOthers(self, partList: list[Instance], overlapIgnored: float) -> bool:
		pass

	@abstractmethod
	def BulkMoveTo(self, partList: list[Instance], cframeList: list[Any], eventMode: BulkMoveMode) -> None:
		pass

	@abstractmethod
	def FindPartOnRay(self, ray: Ray, ignoreDescendantsInstance: Instance, terrainCellsAreCubes: bool, ignoreWater: bool) -> tuple[Any]:
		pass

	@abstractmethod
	def FindPartOnRayWithIgnoreList(self, ray: Ray, ignoreDescendantsTable: list[Instance], terrainCellsAreCubes: bool, ignoreWater: bool) -> tuple[Any]:
		pass

	@abstractmethod
	def FindPartOnRayWithWhitelist(self, ray: Ray, whitelistDescendantsTable: list[Instance], ignoreWater: bool) -> tuple[Any]:
		pass

	@abstractmethod
	def FindPartsInRegion3(self, region: 'Region3', ignoreDescendantsInstance: Instance, maxParts: int) -> list[Instance]:
		pass

	@abstractmethod
	def FindPartsInRegion3WithIgnoreList(self, region: 'Region3', ignoreDescendantsTable: list[Instance], maxParts: int) -> list[Instance]:
		pass

	@abstractmethod
	def FindPartsInRegion3WithWhiteList(self, region: 'Region3', whitelistDescendantsTable: list[Instance], maxParts: int) -> list[Instance]:
		pass

	@abstractmethod
	def GetPartBoundsInBox(self, cframe: CFrame, size: Vector3, overlapParams: 'OverlapParams') -> list[Instance]:
		pass

	@abstractmethod
	def GetPartBoundsInRadius(self, position: Vector3, radius: float, overlapParams: 'OverlapParams') -> list[Instance]:
		pass

	@abstractmethod
	def GetPartsInPart(self, part: BasePart, overlapParams: 'OverlapParams') -> list[Instance]:
		pass

	@abstractmethod
	def IKMoveTo(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float, collisionsMode: IKCollisionsMode) -> None:
		pass

	@abstractmethod
	def IsRegion3Empty(self, region: 'Region3', ignoreDescendentsInstance: Instance) -> bool:
		pass

	@abstractmethod
	def IsRegion3EmptyWithIgnoreList(self, region: 'Region3', ignoreDescendentsTable: list[Instance]) -> bool:
		pass

	@abstractmethod
	def Raycast(self, origin: Vector3, direction: Vector3, raycastParams: 'RaycastParams') -> 'RaycastResult':
		pass

	@abstractmethod
	def SetInsertPoint(self, point: Vector3, ignoreGrid: bool) -> None:
		pass

	@abstractmethod
	def findPartOnRay(self, ray: Ray, ignoreDescendantsInstance: Instance, terrainCellsAreCubes: bool, ignoreWater: bool) -> tuple[Any]:
		pass

	@abstractmethod
	def findPartsInRegion3(self, region: 'Region3', ignoreDescendantsInstance: Instance, maxParts: int) -> list[Instance]:
		pass


	pass

class Workspace(WorldRoot):
	AllowThirdPartySales: bool
	AnimationWeightedBlendFix: NewAnimationRuntimeSetting
	ClientAnimatorThrottling: ClientAnimatorThrottlingMode
	CurrentCamera: Camera
	DistributedGameTime: float
	FallenPartsDestroyHeight: float
	FilteringEnabled: bool
	GlobalWind: Vector3
	Gravity: float
	InterpolationThrottling: InterpolationThrottlingMode
	Retargeting: AnimatorRetargetingMode
	StreamingEnabled: bool
	StreamingMinRadius: int
	StreamingTargetRadius: int
	TouchesUseCollisionGroups: bool
	HumanoidOnlySetCollisionsOnStateChange: HumanoidOnlySetCollisionsOnStateChange
	MeshPartHeadsAndAccessories: MeshPartHeadsAndAccessories
	PhysicsSteppingMethod: PhysicsSteppingMethod
	ReplicateInstanceDestroySetting: ReplicateInstanceDestroySetting
	SignalBehavior: SignalBehavior
	StreamOutBehavior: StreamOutBehavior
	StreamingIntegrityMode: StreamingIntegrityMode
	Terrain: Terrain
	UnionsScaleNonuniformly: UnionsScaleNonuniformly
	@abstractmethod
	def BreakJointsWorkspace(self, objects: list[Instance]) -> None: # Overloading + Overriding
		pass

	@abstractmethod
	def CalculateJumpDistance(self, gravity: float, jumpPower: float, walkSpeed: float) -> float:
		pass

	@abstractmethod
	def CalculateJumpHeight(self, gravity: float, jumpPower: float) -> float:
		pass

	@abstractmethod
	def CalculateJumpPower(self, gravity: float, jumpHeight: float) -> float:
		pass

	@abstractmethod
	def ExperimentalSolverIsEnabled(self) -> bool:
		pass

	@abstractmethod
	def GetNumAwakeParts(self) -> int:
		pass

	@abstractmethod
	def GetPhysicsThrottling(self) -> int:
		pass

	@abstractmethod
	def GetRealPhysicsFPS(self) -> float:
		pass

	@abstractmethod
	def GetServerTimeNow(self) -> float:
		pass

	@abstractmethod
	def JoinToOutsiders(self, objects: list[Instance], jointType: JointCreationMode) -> None:
		pass

	@abstractmethod
	def MakeJointsWorkspace(self, objects: list[Instance]) -> None: # Overloading + Overriding
		pass

	@abstractmethod
	def PGSIsEnabled(self) -> bool:
		pass

	@abstractmethod
	def SetMeshPartHeadsAndAccessories(self, value: 'MeshPartHeadsAndAccessories') -> None:
		pass

	@abstractmethod
	def SetPhysicsThrottleEnabled(self, value: bool) -> None:
		pass

	@abstractmethod
	def UnjoinFromOutsiders(self, objects: list[Instance]) -> None:
		pass

	@abstractmethod
	def ZoomToExtents(self) -> None:
		pass


	pass

class WorldModel(WorldRoot):

	pass

class PackageLink(Instance):
	AutoUpdate: bool
	Creator: str
	PackageAssetName: str
	PackageId: Content
	PermissionLevel: PackagePermission
	Status: str
	VersionNumber: int

	pass

class PackageService(Instance):

	pass

class PackageUIService(Instance):
	@abstractmethod
	def ConvertToPackageUpload(self, uploadUrl: str, cloneInstances: list[Instance], originalInstances: list[Instance]) -> None:
		pass

	@abstractmethod
	def GetPackageInfo(self, packageAssetId: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def PublishPackage(self, packageInstance: Instance) -> None:
		pass

	@abstractmethod
	def SetPackageVersion(self, packageInstance: Instance, versionNumber: int) -> Instance:
		pass


	pass

class Pages(Instance):
	IsFinished: bool
	@abstractmethod
	def GetCurrentPage(self) -> list[Any]:
		pass

	@abstractmethod
	def AdvanceToNextPageAsync(self) -> None:
		pass


	pass

class CatalogPages(Pages):

	pass

class DataStoreKeyPages(Pages):
	Cursor: str

	pass

class DataStoreListingPages(Pages):
	Cursor: str

	pass

class DataStorePages(Pages):

	pass

class DataStoreVersionPages(Pages):

	pass

class FriendPages(Pages):

	pass

class InventoryPages(Pages):

	pass

class EmotesPages(InventoryPages):

	pass

class OutfitPages(Pages):

	pass

class StandardPages(Pages):

	pass

class PartOperationAsset(Instance):

	pass

class ParticleEmitter(Instance):
	Acceleration: Vector3
	Brightness: float
	Color: ColorSequence
	Drag: float
	EmissionDirection: NormalId
	Enabled: bool
	FlipbookFramerate: NumberRange
	FlipbookIncompatible: str
	FlipbookLayout: ParticleFlipbookLayout
	FlipbookMode: ParticleFlipbookMode
	FlipbookStartRandom: bool
	Lifetime: NumberRange
	LightEmission: float
	LightInfluence: float
	LockedToPart: bool
	Orientation: ParticleOrientation
	Rate: float
	RotSpeed: NumberRange
	Rotation: NumberRange
	Shape: ParticleEmitterShape
	ShapeInOut: ParticleEmitterShapeInOut
	ShapePartial: float
	ShapeStyle: ParticleEmitterShapeStyle
	Size: NumberSequence
	Speed: NumberRange
	SpreadAngle: Vector2
	Squash: NumberSequence
	Texture: Content
	TimeScale: float
	Transparency: NumberSequence
	VelocityInheritance: float
	VelocitySpread: float
	ZOffset: float
	@abstractmethod
	def Clear(self) -> None:
		pass

	@abstractmethod
	def Emit(self, particleCount: int) -> None:
		pass

	@abstractmethod
	def FastForward(self, numFrames: int) -> None:
		pass


	pass

class Path(Instance):
	Status: PathStatus
	@abstractmethod
	def GetPointCoordinates(self) -> list[Any]:
		pass

	@abstractmethod
	def GetWaypoints(self) -> list[Any]:
		pass

	@abstractmethod
	def CheckOcclusionAsync(self, start: int) -> int:
		pass

	@abstractmethod
	def ComputeAsync(self, start: Vector3, finish: Vector3) -> None:
		pass


	pass

class PathfindingLink(Instance):
	Attachment0: Attachment
	Attachment1: Attachment
	IsBidirectional: bool
	Label: str

	pass

class PathfindingModifier(Instance):
	Label: str
	PassThrough: bool

	pass

class PathfindingService(Instance):
	EmptyCutoff: float
	@abstractmethod
	def CreatePath(self, agentParameters: dict[Any, Any]) -> Instance:
		pass

	@abstractmethod
	def ComputeRawPathAsync(self, start: Vector3, finish: Vector3, maxDistance: float) -> Instance:
		pass

	@abstractmethod
	def ComputeSmoothPathAsync(self, start: Vector3, finish: Vector3, maxDistance: float) -> Instance:
		pass

	@abstractmethod
	def FindPathAsync(self, start: Vector3, finish: Vector3) -> Instance:
		pass


	pass

class PausedState(Instance):
	AllThreadsPaused: bool
	Reason: DebuggerPauseReason
	ThreadId: int

	pass

class PausedStateBreakpoint(PausedState):
	Breakpoint: Breakpoint

	pass

class PausedStateException(PausedState):
	ExceptionText: str

	pass

class PermissionsService(Instance):
	@abstractmethod
	def GetIsThirdPartyAssetAllowed(self) -> bool:
		pass

	@abstractmethod
	def GetIsThirdPartyPurchaseAllowed(self) -> bool:
		pass

	@abstractmethod
	def GetIsThirdPartyTeleportAllowed(self) -> bool:
		pass

	@abstractmethod
	def GetPermissions(self, assetId: str) -> list[Any]:
		pass

	@abstractmethod
	def SetPermissions(self, assetId: str, permissions: list[Any]) -> None:
		pass


	pass

class PhysicsService(Instance):
	@abstractmethod
	def CollisionGroupContainsPart(self, name: str, part: BasePart) -> bool:
		pass

	@abstractmethod
	def CollisionGroupSetCollidable(self, name1: str, name2: str, collidable: bool) -> None:
		pass

	@abstractmethod
	def CollisionGroupsAreCollidable(self, name1: str, name2: str) -> bool:
		pass

	@abstractmethod
	def CreateCollisionGroup(self, name: str) -> int:
		pass

	@abstractmethod
	def GetCollisionGroupId(self, name: str) -> int:
		pass

	@abstractmethod
	def GetCollisionGroupName(self, name: int) -> str:
		pass

	@abstractmethod
	def GetCollisionGroups(self) -> list[Any]:
		pass

	@abstractmethod
	def GetMaxCollisionGroups(self) -> int:
		pass

	@abstractmethod
	def GetRegisteredCollisionGroups(self) -> list[Any]:
		pass

	@abstractmethod
	def IkSolve(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float) -> None:
		pass

	@abstractmethod
	def IsCollisionGroupRegistered(self, name: str) -> bool:
		pass

	@abstractmethod
	def LocalIkSolve(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float) -> None:
		pass

	@abstractmethod
	def RegisterCollisionGroup(self, name: str) -> None:
		pass

	@abstractmethod
	def RemoveCollisionGroup(self, name: str) -> None:
		pass

	@abstractmethod
	def RenameCollisionGroup(self, from_: str, to: str) -> None:
		pass

	@abstractmethod
	def SetPartCollisionGroup(self, part: BasePart, name: str) -> None:
		pass

	@abstractmethod
	def UnregisterCollisionGroup(self, name: str) -> None:
		pass


	pass

class PhysicsSettings(Instance):
	AllowSleep: bool
	AreAnchorsShown: bool
	AreAssembliesShown: bool
	AreAwakePartsHighlighted: bool
	AreBodyTypesShown: bool
	AreContactIslandsShown: bool
	AreContactPointsShown: bool
	AreJointCoordinatesShown: bool
	AreMechanismsShown: bool
	AreModelCoordsShown: bool
	AreOwnersShown: bool
	ArePartCoordsShown: bool
	AreRegionsShown: bool
	AreTerrainReplicationRegionsShown: bool
	AreTimestepsShown: bool
	AreUnalignedPartsShown: bool
	AreWorldCoordsShown: bool
	DisableCSGv2: bool
	ForceCSGv2: bool
	IsInterpolationThrottleShown: bool
	IsReceiveAgeShown: bool
	IsTreeShown: bool
	PhysicsEnvironmentalThrottle: EnviromentalPhysicsThrottle
	ShowDecompositionGeometry: bool
	ThrottleAdjustTime: float
	UseCSGv2: bool

	pass

class Player(Instance):
	AccountAge: int
	AppearanceDidLoad: bool
	AutoJumpEnabled: bool
	CameraMaxZoomDistance: float
	CameraMinZoomDistance: float
	CanLoadCharacterAppearance: bool
	Character: Model
	CharacterAppearance: str
	CharacterAppearanceId: int
	DataComplexity: int
	DataComplexityLimit: int
	DataReady: bool
	DevComputerCameraMode: DevComputerCameraMovementMode
	DevEnableMouseLock: bool
	DevTouchCameraMode: DevTouchCameraMovementMode
	DisplayName: str
	FollowUserId: int
	GameplayPaused: bool
	Guest: bool
	HealthDisplayDistance: float
	LocaleId: str
	MaximumSimulationRadius: float
	NameDisplayDistance: float
	Neutral: bool
	OsPlatform: str
	PlatformName: str
	ReplicationFocus: Instance
	RespawnLocation: SpawnLocation
	SimulationRadius: float
	Team: 'Team'
	TeamColor: BrickColor
	Teleported: bool
	TeleportedIn: bool
	UnfilteredChat: bool
	UserId: int
	VRDevice: str
	userId: int
	CameraMode: CameraMode
	ChatMode: ChatMode
	DevCameraOcclusionMode: DevCameraOcclusionMode
	DevComputerMovementMode: DevComputerMovementMode
	DevTouchMovementMode: DevTouchMovementMode
	MembershipType: MembershipType
	@abstractmethod
	def AddToBlockList(self, userIds: list[Any]) -> None:
		pass

	@abstractmethod
	def ClearCharacterAppearance(self) -> None:
		pass

	@abstractmethod
	def DistanceFromCharacter(self, point: Vector3) -> float:
		pass

	@abstractmethod
	def GetFriendStatus(self, player: Self) -> FriendStatus:
		pass

	@abstractmethod
	def GetGameSessionID(self) -> str:
		pass

	@abstractmethod
	def GetJoinData(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetMouse(self) -> Mouse:
		pass

	@abstractmethod
	def GetNetworkPing(self) -> float:
		pass

	@abstractmethod
	def GetUnder13(self) -> bool:
		pass

	@abstractmethod
	def HasAppearanceLoaded(self) -> bool:
		pass

	@abstractmethod
	def Kick(self, message: str) -> None:
		pass

	@abstractmethod
	def LoadBoolean(self, key: str) -> bool:
		pass

	@abstractmethod
	def LoadCharacterAppearance(self, assetInstance: Instance) -> None:
		pass

	@abstractmethod
	def LoadData(self) -> None:
		pass

	@abstractmethod
	def LoadInstance(self, key: str) -> Instance:
		pass

	@abstractmethod
	def LoadNumber(self, key: str) -> float:
		pass

	@abstractmethod
	def LoadString(self, key: str) -> str:
		pass

	@abstractmethod
	def Move(self, walkDirection: Vector3, relativeToCamera: bool) -> None:
		pass

	@abstractmethod
	def RemoveCharacter(self) -> None:
		pass

	@abstractmethod
	def RequestFriendship(self, player: Self) -> None:
		pass

	@abstractmethod
	def RevokeFriendship(self, player: Self) -> None:
		pass

	@abstractmethod
	def SaveBoolean(self, key: str, value: bool) -> None:
		pass

	@abstractmethod
	def SaveData(self) -> None:
		pass

	@abstractmethod
	def SaveInstance(self, key: str, value: Instance) -> None:
		pass

	@abstractmethod
	def SaveNumber(self, key: str, value: float) -> None:
		pass

	@abstractmethod
	def SaveString(self, key: str, value: str) -> None:
		pass

	@abstractmethod
	def SetAccountAge(self, accountAge: int) -> None:
		pass

	@abstractmethod
	def SetCharacterAppearanceJson(self, jsonBlob: str) -> None:
		pass

	@abstractmethod
	def SetExperienceSettingsLocaleId(self, locale: str) -> None:
		pass

	@abstractmethod
	def SetMembershipType(self, membershipType: 'MembershipType') -> None:
		pass

	@abstractmethod
	def SetModerationAccessKey(self, moderationAccessKey: str) -> None:
		pass

	@abstractmethod
	def SetSuperSafeChat(self, value: bool) -> None:
		pass

	@abstractmethod
	def SetUnder13(self, value: bool) -> None:
		pass

	@abstractmethod
	def UpdatePlayerBlocked(self, userId: int, blocked: bool) -> None:
		pass

	@abstractmethod
	def loadBoolean(self, key: str) -> bool:
		pass

	@abstractmethod
	def loadInstance(self, key: str) -> Instance:
		pass

	@abstractmethod
	def loadNumber(self, key: str) -> float:
		pass

	@abstractmethod
	def loadString(self, key: str) -> str:
		pass

	@abstractmethod
	def saveBoolean(self, key: str, value: bool) -> None:
		pass

	@abstractmethod
	def saveInstance(self, key: str, value: Instance) -> None:
		pass

	@abstractmethod
	def saveNumber(self, key: str, value: float) -> None:
		pass

	@abstractmethod
	def saveString(self, key: str, value: str) -> None:
		pass

	@abstractmethod
	def GetFriendsOnline(self, maxFriends: int) -> list[Any]:
		pass

	@abstractmethod
	def GetRankInGroup(self, groupId: int) -> int:
		pass

	@abstractmethod
	def GetRoleInGroup(self, groupId: int) -> str:
		pass

	@abstractmethod
	def IsBestFriendsWith(self, userId: int) -> bool:
		pass

	@abstractmethod
	def IsFriendsWith(self, userId: int) -> bool:
		pass

	@abstractmethod
	def IsInGroup(self, groupId: int) -> bool:
		pass

	@abstractmethod
	def LoadCharacter(self) -> None:
		pass

	@abstractmethod
	def LoadCharacterBlocking(self) -> None:
		pass

	@abstractmethod
	def LoadCharacterWithHumanoidDescription(self, humanoidDescription: HumanoidDescription) -> None:
		pass

	@abstractmethod
	def RequestStreamAroundAsync(self, position: Vector3, timeOut: float) -> None:
		pass

	@abstractmethod
	def WaitForDataReady(self) -> bool:
		pass

	@abstractmethod
	def isFriendsWith(self, userId: int) -> bool:
		pass

	@abstractmethod
	def waitForDataReady(self) -> bool:
		pass


	pass

class PlayerEmulatorService(Instance):
	CustomPoliciesEnabled: bool
	EmulatedCountryCode: str
	EmulatedGameLocale: str
	PlayerEmulationEnabled: bool
	SerializedEmulatedPolicyInfo: BinaryString
	@abstractmethod
	def GetEmulatedPolicyInfo(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def RegionCodeWillHaveAutomaticNonCustomPolicies(self, regionCode: str) -> bool:
		pass

	@abstractmethod
	def SetEmulatedPolicyInfo(self, emulatedPolicyInfo: dict[Any, Any]) -> None:
		pass


	pass

class PlayerScripts(Instance):
	@abstractmethod
	def ClearComputerCameraMovementModes(self) -> None:
		pass

	@abstractmethod
	def ClearComputerMovementModes(self) -> None:
		pass

	@abstractmethod
	def ClearTouchCameraMovementModes(self) -> None:
		pass

	@abstractmethod
	def ClearTouchMovementModes(self) -> None:
		pass

	@abstractmethod
	def GetRegisteredComputerCameraMovementModes(self) -> list[Any]:
		pass

	@abstractmethod
	def GetRegisteredComputerMovementModes(self) -> list[Any]:
		pass

	@abstractmethod
	def GetRegisteredTouchCameraMovementModes(self) -> list[Any]:
		pass

	@abstractmethod
	def GetRegisteredTouchMovementModes(self) -> list[Any]:
		pass

	@abstractmethod
	def RegisterComputerCameraMovementMode(self, cameraMovementMode: ComputerCameraMovementMode) -> None:
		pass

	@abstractmethod
	def RegisterComputerMovementMode(self, movementMode: ComputerMovementMode) -> None:
		pass

	@abstractmethod
	def RegisterTouchCameraMovementMode(self, cameraMovementMode: TouchCameraMovementMode) -> None:
		pass

	@abstractmethod
	def RegisterTouchMovementMode(self, movementMode: TouchMovementMode) -> None:
		pass


	pass

class Players(Instance):
	BubbleChat: bool
	CharacterAutoLoads: bool
	ClassicChat: bool
	LocalPlayer: Player
	MaxPlayers: int
	MaxPlayersInternal: int
	NumPlayers: int
	PreferredPlayers: int
	PreferredPlayersInternal: int
	RespawnTime: float
	localPlayer: Player
	numPlayers: int
	@abstractmethod
	def Chat(self, message: str) -> None:
		pass

	@abstractmethod
	def CreateLocalPlayer(self) -> Player:
		pass

	@abstractmethod
	def GetPlayerByUserId(self, userId: int) -> Player:
		pass

	@abstractmethod
	def GetPlayerFromCharacter(self, character: Model) -> Player:
		pass

	@abstractmethod
	def GetPlayers(self) -> list[Instance]:
		pass

	@abstractmethod
	def ReportAbuse(self, player: Player, reason: str, optionalMessage: str) -> None:
		pass

	@abstractmethod
	def ReportAbuseV3(self, player: Player, jsonTags: str) -> None:
		pass

	@abstractmethod
	def SetChatStyle(self, style: ChatStyle) -> None:
		pass

	@abstractmethod
	def SetLocalPlayerInfo(self, userId: int, userName: str, displayName: str, membershipType: MembershipType, isUnder13: bool) -> None:
		pass

	@abstractmethod
	def TeamChat(self, message: str) -> None:
		pass

	@abstractmethod
	def WhisperChat(self, message: str, player: Instance) -> None:
		pass

	@abstractmethod
	def getPlayers(self) -> list[Instance]:
		pass

	@abstractmethod
	def playerFromCharacter(self, character: Model) -> Player:
		pass

	@abstractmethod
	def players(self) -> list[Instance]:
		pass

	@abstractmethod
	def CreateHumanoidModelFromDescription(self, description: HumanoidDescription, rigType: HumanoidRigType, assetTypeVerification: AssetTypeVerification) -> Model:
		pass

	@abstractmethod
	def CreateHumanoidModelFromUserId(self, userId: int) -> Model:
		pass

	@abstractmethod
	def GetCharacterAppearanceAsync(self, userId: int) -> Model:
		pass

	@abstractmethod
	def GetCharacterAppearanceInfoAsync(self, userId: int) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetFriendsAsync(self, userId: int) -> FriendPages:
		pass

	@abstractmethod
	def GetHumanoidDescriptionFromOutfitId(self, outfitId: int) -> HumanoidDescription:
		pass

	@abstractmethod
	def GetHumanoidDescriptionFromUserId(self, userId: int) -> HumanoidDescription:
		pass

	@abstractmethod
	def GetNameFromUserIdAsync(self, userId: int) -> str:
		pass

	@abstractmethod
	def GetUserIdFromNameAsync(self, userName: str) -> int:
		pass

	@abstractmethod
	def GetUserThumbnailAsync(self, userId: int, thumbnailType: ThumbnailType, thumbnailSize: ThumbnailSize) -> tuple[Any]:
		pass


	pass

class Plugin(Instance):
	CollisionEnabled: bool
	GridSize: float
	HostDataModelType: StudioDataModelType
	HostDataModelTypeIsCurrent: bool
	UsesAssetInsertionDrag: bool
	MultipleDocumentInterfaceInstance: MultipleDocumentInterfaceInstance
	@abstractmethod
	def Activate(self, exclusiveMouse: bool) -> None:
		pass

	@abstractmethod
	def CreatePluginAction(self, actionId: str, text: str, statusTip: str, iconName: str, allowBinding: bool) -> 'PluginAction':
		pass

	@abstractmethod
	def CreatePluginMenu(self, id: str, title: str, icon: str) -> 'PluginMenu':
		pass

	@abstractmethod
	def CreateToolbar(self, name: str) -> 'PluginToolbar':
		pass

	@abstractmethod
	def Deactivate(self) -> None:
		pass

	@abstractmethod
	def GetItem(self, key: str, defaultValue: Any) -> Any:
		pass

	@abstractmethod
	def GetJoinMode(self) -> JointCreationMode:
		pass

	@abstractmethod
	def GetMouse(self) -> PluginMouse:
		pass

	@abstractmethod
	def GetSelectedRibbonTool(self) -> RibbonTool:
		pass

	@abstractmethod
	def GetSetting(self, key: str) -> Any:
		pass

	@abstractmethod
	def GetStudioUserId(self) -> int:
		pass

	@abstractmethod
	def Invoke(self, key: str, arguments: tuple[Any]) -> None:
		pass

	@abstractmethod
	def IsActivated(self) -> bool:
		pass

	@abstractmethod
	def IsActivatedWithExclusiveMouse(self) -> bool:
		pass

	@abstractmethod
	def Negate(self, objects: list[Instance]) -> list[Instance]:
		pass

	@abstractmethod
	def OnInvoke(self, key: str, callback: Callable[..., Any]) -> Instance:
		pass

	@abstractmethod
	def OnSetItem(self, key: str, callback: Callable[..., Any]) -> Instance:
		pass

	@abstractmethod
	def OpenScript(self, script: LuaSourceContainer, lineNumber: int) -> None:
		pass

	@abstractmethod
	def OpenWikiPage(self, url: str) -> None:
		pass

	@abstractmethod
	def PauseSound(self, sound: Instance) -> None:
		pass

	@abstractmethod
	def PlaySound(self, sound: Instance, normalizedTimePosition: float) -> None:
		pass

	@abstractmethod
	def ResumeSound(self, sound: Instance) -> None:
		pass

	@abstractmethod
	def SaveSelectedToRoblox(self) -> None:
		pass

	@abstractmethod
	def SelectRibbonTool(self, tool: RibbonTool, position: UDim2) -> None:
		pass

	@abstractmethod
	def Separate(self, objects: list[Instance]) -> list[Instance]:
		pass

	@abstractmethod
	def SetItem(self, key: str, value: Any) -> None:
		pass

	@abstractmethod
	def SetReady(self) -> None:
		pass

	@abstractmethod
	def SetSetting(self, key: str, value: Any) -> None:
		pass

	@abstractmethod
	def StartDecalDrag(self, decal: Instance) -> None:
		pass

	@abstractmethod
	def StartDrag(self, dragData: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def StopAllSounds(self) -> None:
		pass

	@abstractmethod
	def Union(self, objects: list[Instance]) -> Instance:
		pass

	@abstractmethod
	def CreateDockWidgetPluginGui(self, pluginGuiId: str, dockWidgetPluginGuiInfo: 'DockWidgetPluginGuiInfo') -> DockWidgetPluginGui:
		pass

	@abstractmethod
	def CreateQWidgetPluginGui(self, pluginGuiId: str, pluginGuiOptions: dict[Any, Any]) -> QWidgetPluginGui:
		pass

	@abstractmethod
	def ImportFbxAnimation(self, rigModel: Instance, isR15: bool) -> Instance:
		pass

	@abstractmethod
	def ImportFbxRig(self, isR15: bool) -> Instance:
		pass

	@abstractmethod
	def PromptForExistingAssetId(self, assetType: str) -> int:
		pass

	@abstractmethod
	def PromptSaveSelection(self, suggestedFileName: str) -> bool:
		pass


	pass

class PluginAction(Instance):
	ActionId: str
	AllowBinding: bool
	Checked: bool
	DefaultShortcut: str
	Enabled: bool
	StatusTip: str
	Text: str

	pass

class PluginDebugService(Instance):

	pass

class PluginDragEvent(Instance):
	Data: str
	MimeType: str
	Position: Vector2
	Sender: str

	pass

class PluginGuiService(Instance):

	pass

class PluginManagementService(Instance):
	@abstractmethod
	def SetAutoUpdate(self, pluginId: int, state: bool) -> None:
		pass


	pass

class PluginManager(Instance):
	@abstractmethod
	def CreatePlugin(self) -> Instance:
		pass

	@abstractmethod
	def ExportPlace(self, filePath: str) -> None:
		pass

	@abstractmethod
	def ExportSelection(self, filePath: str) -> None:
		pass


	pass

class PluginManagerInterface(Instance):
	@abstractmethod
	def CreatePlugin(self) -> Instance:
		pass

	@abstractmethod
	def ExportPlace(self, filePath: str) -> None:
		pass

	@abstractmethod
	def ExportSelection(self, filePath: str) -> None:
		pass


	pass

class PluginMenu(Instance):
	Icon: str
	Title: str
	@abstractmethod
	def AddAction(self, action: Instance) -> None:
		pass

	@abstractmethod
	def AddMenu(self, menu: Instance) -> None:
		pass

	@abstractmethod
	def AddNewAction(self, actionId: str, text: str, icon: str) -> Instance:
		pass

	@abstractmethod
	def AddSeparator(self) -> None:
		pass

	@abstractmethod
	def Clear(self) -> None:
		pass

	@abstractmethod
	def ShowAsync(self) -> Instance:
		pass


	pass

class PluginPolicyService(Instance):
	@abstractmethod
	def GetPluginPolicy(self, pluginName: str) -> dict[Any, Any]:
		pass


	pass

class PluginToolbar(Instance):
	@abstractmethod
	def CreateButton(self, buttonId: str, tooltip: str, iconname: str, text: str) -> Instance:
		pass


	pass

class PluginToolbarButton(Instance):
	ClickableWhenViewportHidden: bool
	Enabled: bool
	Icon: Content
	@abstractmethod
	def SetActive(self, active: bool) -> None:
		pass


	pass

class PointsService(Instance):
	@abstractmethod
	def GetAwardablePoints(self) -> int:
		pass

	@abstractmethod
	def AwardPoints(self, userId: int, amount: int) -> tuple[Any]:
		pass

	@abstractmethod
	def GetGamePointBalance(self, userId: int) -> int:
		pass

	@abstractmethod
	def GetPointBalance(self, userId: int) -> int:
		pass


	pass

class PolicyService(Instance):
	IsLuobuServer: TriStateBoolean
	LuobuWhitelisted: TriStateBoolean
	@abstractmethod
	def GetPolicyInfoForPlayerAsync(self, player: Instance) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetPolicyInfoForServerRobloxOnlyAsync(self) -> dict[Any, Any]:
		pass


	pass

class PoseBase(Instance):
	EasingDirection: PoseEasingDirection
	EasingStyle: PoseEasingStyle
	Weight: float

	pass

class NumberPose(PoseBase):
	Value: float

	pass

class Pose(PoseBase):
	MaskWeight: float
	CFrame: CFrame
	@abstractmethod
	def AddSubPose(self, pose: Instance) -> None:
		pass

	@abstractmethod
	def GetSubPoses(self) -> list[Instance]:
		pass

	@abstractmethod
	def RemoveSubPose(self, pose: Instance) -> None:
		pass


	pass

class PostEffect(Instance):
	Enabled: bool

	pass

class BloomEffect(PostEffect):
	Intensity: float
	Size: float
	Threshold: float

	pass

class BlurEffect(PostEffect):
	Size: float

	pass

class ColorCorrectionEffect(PostEffect):
	Brightness: float
	Contrast: float
	Saturation: float
	TintColor: Color3

	pass

class DepthOfFieldEffect(PostEffect):
	FarIntensity: float
	FocusDistance: float
	InFocusRadius: float
	NearIntensity: float

	pass

class SunRaysEffect(PostEffect):
	Intensity: float
	Spread: float

	pass

class ProcessInstancePhysicsService(Instance):

	pass

class ProximityPrompt(Instance):
	ActionText: str
	AutoLocalize: bool
	ClickablePrompt: bool
	Enabled: bool
	Exclusivity: ProximityPromptExclusivity
	GamepadKeyCode: KeyCode
	HoldDuration: float
	KeyboardKeyCode: KeyCode
	MaxActivationDistance: float
	ObjectText: str
	RequiresLineOfSight: bool
	RootLocalizationTable: LocalizationTable
	Style: ProximityPromptStyle
	UIOffset: Vector2
	@abstractmethod
	def InputHoldBegin(self) -> None:
		pass

	@abstractmethod
	def InputHoldEnd(self) -> None:
		pass


	pass

class ProximityPromptService(Instance):
	Enabled: bool
	MaxPromptsVisible: int

	pass

class PublishService(Instance):
	@abstractmethod
	def PublishDescendantAssets(self, instance: Instance) -> bool:
		pass

	@abstractmethod
	def PublishCageMeshAsync(self, wrap: Instance, cageType: CageType) -> Content:
		pass


	pass

class RbxAnalyticsService(Instance):
	@abstractmethod
	def AddGlobalPointsField(self, key: str, value: int) -> None:
		pass

	@abstractmethod
	def AddGlobalPointsTag(self, key: str, value: str) -> None:
		pass

	@abstractmethod
	def DEPRECATED_TrackEvent(self, category: str, action: str, label: str, value: int) -> None:
		pass

	@abstractmethod
	def DEPRECATED_TrackEventWithArgs(self, category: str, action: str, label: str, args: dict[Any, Any], value: int) -> None:
		pass

	@abstractmethod
	def GetClientId(self) -> str:
		pass

	@abstractmethod
	def GetSessionId(self) -> str:
		pass

	@abstractmethod
	def ReleaseRBXEventStream(self, target: str) -> None:
		pass

	@abstractmethod
	def RemoveGlobalPointsField(self, key: str) -> None:
		pass

	@abstractmethod
	def RemoveGlobalPointsTag(self, key: str) -> None:
		pass

	@abstractmethod
	def ReportCounter(self, counterName: str, amount: int) -> None:
		pass

	@abstractmethod
	def ReportInfluxSeries(self, seriesName: str, points: dict[Any, Any], throttlingPercentage: int) -> None:
		pass

	@abstractmethod
	def ReportStats(self, category: str, value: float) -> None:
		pass

	@abstractmethod
	def ReportToDiagByCountryCode(self, featureName: str, measureName: str, seconds: float) -> None:
		pass

	@abstractmethod
	def SendEventDeferred(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SendEventImmediately(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SetRBXEvent(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def SetRBXEventStream(self, target: str, eventContext: str, eventName: str, additionalArgs: dict[Any, Any]) -> None:
		pass

	@abstractmethod
	def TrackEvent(self, category: str, action: str, label: str, value: int) -> None:
		pass

	@abstractmethod
	def TrackEventWithArgs(self, category: str, action: str, label: str, args: dict[Any, Any], value: int) -> None:
		pass

	@abstractmethod
	def UpdateHeartbeatObject(self, args: dict[Any, Any]) -> None:
		pass


	pass

class ReflectionMetadata(Instance):

	pass

class ReflectionMetadataCallbacks(Instance):

	pass

class ReflectionMetadataClasses(Instance):

	pass

class ReflectionMetadataEnums(Instance):

	pass

class ReflectionMetadataEvents(Instance):

	pass

class ReflectionMetadataFunctions(Instance):

	pass

class ReflectionMetadataItem(Instance):
	Browsable: bool
	ClassCategory: str
	ClientOnly: bool
	Constraint: str
	Deprecated: bool
	EditingDisabled: bool
	EditorType: str
	FFlag: str
	IsBackend: bool
	PropertyOrder: int
	ScriptContext: str
	ServerOnly: bool
	SliderScaling: str
	UIMaximum: float
	UIMinimum: float
	UINumTicks: float

	pass

class ReflectionMetadataClass(ReflectionMetadataItem):
	ExplorerImageIndex: int
	ExplorerOrder: int
	Insertable: bool
	PreferredParent: str

	pass

class ReflectionMetadataEnum(ReflectionMetadataItem):

	pass

class ReflectionMetadataEnumItem(ReflectionMetadataItem):

	pass

class ReflectionMetadataMember(ReflectionMetadataItem):

	pass

class ReflectionMetadataProperties(Instance):

	pass

class ReflectionMetadataYieldFunctions(Instance):

	pass

class RemoteDebuggerServer(Instance):

	pass

class RemoteEvent(Instance):
	@abstractmethod
	def FireAllClients(self, arguments: tuple[Any]) -> None:
		pass

	@abstractmethod
	def FireClient(self, player: Player, arguments: tuple[Any]) -> None:
		pass

	@abstractmethod
	def FireServer(self, arguments: tuple[Any]) -> None:
		pass


	pass

class RemoteFunction(Instance):
	@abstractmethod
	def InvokeClient(self, player: Player, arguments: tuple[Any]) -> tuple[Any]:
		pass

	@abstractmethod
	def InvokeServer(self, arguments: tuple[Any]) -> tuple[Any]:
		pass


	pass

class RenderSettings(Instance):
	AutoFRMLevel: int
	EagerBulkExecution: bool
	EditQualityLevel: QualityLevel
	EnableFRM: bool
	ExportMergeByMaterial: bool
	FrameRateManager: FramerateManagerMode
	MeshCacheSize: int
	ReloadAssets: bool
	RenderCSGTrianglesDebug: bool
	ShowBoundingBoxes: bool
	GraphicsMode: GraphicsMode
	MeshPartDetailLevel: MeshPartDetailLevel
	QualityLevel: QualityLevel
	@abstractmethod
	def GetMaxQualityLevel(self) -> int:
		pass


	pass

class RenderingTest(Instance):
	ComparisonDiffThreshold: int
	ComparisonMethod: RenderingTestComparisonMethod
	ComparisonPsnrThreshold: float
	Description: str
	FieldOfView: float
	Orientation: Vector3
	Position: Vector3
	QualityLevel: int
	ShouldSkip: bool
	Ticket: str
	CFrame: CFrame
	@abstractmethod
	def RenderdocTriggerCapture(self) -> None:
		pass


	pass

class ReplicatedFirst(Instance):
	@abstractmethod
	def IsDefaultLoadingGuiRemoved(self) -> bool:
		pass

	@abstractmethod
	def IsFinishedReplicating(self) -> bool:
		pass

	@abstractmethod
	def RemoveDefaultLoadingScreen(self) -> None:
		pass

	@abstractmethod
	def SetDefaultLoadingGuiRemoved(self) -> None:
		pass


	pass

class ReplicatedStorage(Instance):

	pass

class RobloxPluginGuiService(Instance):

	pass

class RobloxReplicatedStorage(Instance):

	pass

class RotationCurve(Instance):
	Length: int
	@abstractmethod
	def GetKeyAtIndex(self, index: int) -> 'RotationCurveKey':
		pass

	@abstractmethod
	def GetKeyIndicesAtTime(self, time: float) -> list[Any]:
		pass

	@abstractmethod
	def GetKeys(self) -> list[Any]:
		pass

	@abstractmethod
	def GetValueAtTime(self, time: float) -> CoordinateFrame| None:
		pass

	@abstractmethod
	def InsertKey(self, key: 'RotationCurveKey') -> list[Any]:
		pass

	@abstractmethod
	def RemoveKeyAtIndex(self, startingIndex: int, count: int) -> int:
		pass

	@abstractmethod
	def SetKeys(self, keys: list[Any]) -> int:
		pass


	pass

class RtMessagingService(Instance):

	pass

class RunService(Instance):
	ClientGitHash: str
	@abstractmethod
	def BindToRenderStep(self, name: str, priority: int, function: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def GetCoreScriptVersion(self) -> str:
		pass

	@abstractmethod
	def GetRobloxClientChannel(self) -> str:
		pass

	@abstractmethod
	def GetRobloxVersion(self) -> str:
		pass

	@abstractmethod
	def IsClient(self) -> bool:
		pass

	@abstractmethod
	def IsEdit(self) -> bool:
		pass

	@abstractmethod
	def IsRunMode(self) -> bool:
		pass

	@abstractmethod
	def IsRunning(self) -> bool:
		pass

	@abstractmethod
	def IsServer(self) -> bool:
		pass

	@abstractmethod
	def IsStudio(self) -> bool:
		pass

	@abstractmethod
	def Pause(self) -> None:
		pass

	@abstractmethod
	def Reset(self) -> None:
		pass

	@abstractmethod
	def Run(self) -> None:
		pass

	@abstractmethod
	def Set3dRenderingEnabled(self, enable: bool) -> None:
		pass

	@abstractmethod
	def SetRobloxGuiFocused(self, focus: bool) -> None:
		pass

	@abstractmethod
	def Stop(self) -> None:
		pass

	@abstractmethod
	def UnbindFromRenderStep(self, name: str) -> None:
		pass

	@abstractmethod
	def setThrottleFramerateEnabled(self, enable: bool) -> None:
		pass


	pass

class RuntimeScriptService(Instance):

	pass

class ScreenshotHud(Instance):
	CameraButtonIcon: Content
	CameraButtonPosition: UDim2
	CloseButtonPosition: UDim2
	CloseWhenScreenshotTaken: bool
	ExperienceNameOverlayEnabled: bool
	OverlayFont: Font
	UsernameOverlayEnabled: bool
	Visible: bool

	pass

class ScriptBuilder(Instance):

	pass

class CoreScriptBuilder(ScriptBuilder):

	pass

class ScriptChangeService(Instance):

	pass

class ScriptCloneWatcher(Instance):

	pass

class ScriptCloneWatcherHelper(Instance):

	pass

class ScriptContext(Instance):
	ScriptsDisabled: bool
	@abstractmethod
	def AddCoreScriptLocal(self, name: str, parent: Instance) -> None:
		pass

	@abstractmethod
	def ClearScriptProfilingData(self) -> None:
		pass

	@abstractmethod
	def DeserializeScriptProfilerString(self, jsonString: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetCoverageStats(self) -> list[Any]:
		pass

	@abstractmethod
	def SaveScriptProfilingData(self, filename: str) -> None:
		pass

	@abstractmethod
	def SetTimeout(self, seconds: float) -> None:
		pass

	@abstractmethod
	def StartScriptProfiling(self) -> None:
		pass

	@abstractmethod
	def StopScriptProfiling(self) -> dict[Any, Any]:
		pass


	pass

class ScriptDebugger(Instance):
	CurrentLine: int
	IsDebugging: bool
	IsPaused: bool
	Script: Instance
	@abstractmethod
	def AddWatch(self, expression: str) -> Instance:
		pass

	@abstractmethod
	def GetBreakpoints(self) -> list[Instance]:
		pass

	@abstractmethod
	def GetGlobals(self, stackFrame: int) -> 'Map':
		pass

	@abstractmethod
	def GetLocals(self, stackFrame: int) -> 'Map':
		pass

	@abstractmethod
	def GetStack(self) -> list[Any]:
		pass

	@abstractmethod
	def GetUpvalues(self, stackFrame: int) -> 'Map':
		pass

	@abstractmethod
	def GetWatchValue(self, watch: Instance) -> Any:
		pass

	@abstractmethod
	def GetWatches(self) -> list[Instance]:
		pass

	@abstractmethod
	def SetBreakpoint(self, line: int, isContextDependentBreakpoint: bool) -> Instance:
		pass

	@abstractmethod
	def SetGlobal(self, name: str, value: Any, stackFrame: int) -> None:
		pass

	@abstractmethod
	def SetLocal(self, name: str, value: Any, stackFrame: int) -> None:
		pass

	@abstractmethod
	def SetUpvalue(self, name: str, value: Any, stackFrame: int) -> None:
		pass


	pass

class ScriptDocument(Instance):
	@abstractmethod
	def GetInternalUri(self) -> str:
		pass

	@abstractmethod
	def GetLine(self, lineIndex: int| None) -> str:
		pass

	@abstractmethod
	def GetLineCount(self) -> int:
		pass

	@abstractmethod
	def GetScript(self) -> LuaSourceContainer:
		pass

	@abstractmethod
	def GetSelectedText(self) -> str:
		pass

	@abstractmethod
	def GetSelection(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetSelectionEnd(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetSelectionStart(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetText(self, startLine: int| None, startCharacter: int| None, endLine: int| None, endCharacter: int| None) -> str:
		pass

	@abstractmethod
	def GetViewport(self) -> tuple[Any]:
		pass

	@abstractmethod
	def HasSelectedText(self) -> bool:
		pass

	@abstractmethod
	def IsCommandBar(self) -> bool:
		pass

	@abstractmethod
	def CloseAsync(self) -> tuple[Any]:
		pass

	@abstractmethod
	def EditTextAsync(self, newText: str, startLine: int, startCharacter: int, endLine: int, endCharacter: int) -> tuple[Any]:
		pass

	@abstractmethod
	def ForceSetSelectionAsync(self, cursorLine: int, cursorCharacter: int, anchorLine: int| None, anchorCharacter: int| None) -> tuple[Any]:
		pass

	@abstractmethod
	def RequestSetSelectionAsync(self, cursorLine: int, cursorCharacter: int, anchorLine: int| None, anchorCharacter: int| None) -> tuple[Any]:
		pass


	pass

class ScriptEditorService(Instance):
	@abstractmethod
	def DeregisterAutocompleteCallback(self, name: str) -> None:
		pass

	@abstractmethod
	def FindScriptDocument(self, script: LuaSourceContainer) -> ScriptDocument:
		pass

	@abstractmethod
	def GetScriptDocuments(self) -> list[Instance]:
		pass

	@abstractmethod
	def RegisterAutocompleteCallback(self, name: str, priority: int, callbackFunction: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def OpenScriptDocumentAsync(self, script: LuaSourceContainer) -> tuple[Any]:
		pass


	pass

class ScriptRegistrationService(Instance):
	@abstractmethod
	def GetSourceContainerByScriptGuid(self, guid: str) -> LuaSourceContainer:
		pass


	pass

class ScriptService(Instance):

	pass

class Selection(Instance):
	ActiveInstance: Instance
	SelectionLineThickness: int
	SelectionThickness: float
	@abstractmethod
	def Add(self, instancesToAdd: list[Instance]) -> None:
		pass

	@abstractmethod
	def ClearTerrainSelectionHack(self) -> None:
		pass

	@abstractmethod
	def Get(self) -> list[Instance]:
		pass

	@abstractmethod
	def RemoveSelection(self, instancesToRemove: list[Instance]) -> None: # Overloading + Overriding
		pass

	@abstractmethod
	def Set(self, selection: list[Instance]) -> None:
		pass

	@abstractmethod
	def SetTerrainSelectionHack(self, center: Vector3, size: Vector3) -> None:
		pass


	pass

class ServerScriptService(Instance):
	LoadStringEnabled: bool

	pass

class ServerStorage(Instance):

	pass

class ServiceProvider(Instance):
	@abstractmethod
	def FindService(self, className: str) -> Instance:
		pass

	@abstractmethod
	def GetService(self, className: str) -> Instance:
		pass

	@abstractmethod
	def getService(self, className: str) -> Instance:
		pass

	@abstractmethod
	def service(self, className: str) -> Instance:
		pass


	pass

class DataModel(ServiceProvider):
	CreatorId: int
	GameId: int
	IsSFFlagsLoaded: bool
	JobId: str
	PlaceId: int
	PlaceVersion: int
	PrivateServerId: str
	PrivateServerOwnerId: int
	VIPServerId: str
	VIPServerOwnerId: int
	lighting: Instance
	workspace: Workspace
	CreatorType: CreatorType
	GearGenreSetting: GearGenreSetting
	Genre: Genre
	Workspace: Workspace
	@abstractmethod
	def BindToClose(self, function: Callable[..., Any]) -> None:
		pass

	@abstractmethod
	def DefineFastFlag(self, name: str, defaultValue: bool) -> bool:
		pass

	@abstractmethod
	def DefineFastInt(self, name: str, defaultValue: int) -> int:
		pass

	@abstractmethod
	def DefineFastString(self, name: str, defaultValue: str) -> str:
		pass

	@abstractmethod
	def GetEngineFeature(self, name: str) -> bool:
		pass

	@abstractmethod
	def GetFastFlag(self, name: str) -> bool:
		pass

	@abstractmethod
	def GetFastInt(self, name: str) -> int:
		pass

	@abstractmethod
	def GetFastString(self, name: str) -> str:
		pass

	@abstractmethod
	def GetJobsInfo(self) -> list[Any]:
		pass

	@abstractmethod
	def GetMessage(self) -> str:
		pass

	@abstractmethod
	def GetObjects(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def GetObjectsAllOrNone(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def GetObjectsList(self, urls: list[Any]) -> list[Any]:
		pass

	@abstractmethod
	def GetRemoteBuildMode(self) -> bool:
		pass

	@abstractmethod
	def IsGearTypeAllowed(self, gearType: GearType) -> bool:
		pass

	@abstractmethod
	def IsLoaded(self) -> bool:
		pass

	@abstractmethod
	def Load(self, url: Content) -> None:
		pass

	@abstractmethod
	def OpenScreenshotsFolder(self) -> None:
		pass

	@abstractmethod
	def OpenVideosFolder(self) -> None:
		pass

	@abstractmethod
	def ReportInGoogleAnalytics(self, category: str, action: str, label: str, value: int) -> None:
		pass

	@abstractmethod
	def SetFastFlagForTesting(self, name: str, newValue: bool) -> bool:
		pass

	@abstractmethod
	def SetFastIntForTesting(self, name: str, newValue: int) -> int:
		pass

	@abstractmethod
	def SetFastStringForTesting(self, name: str, newValue: str) -> str:
		pass

	@abstractmethod
	def SetPlaceId(self, placeId: int) -> None:
		pass

	@abstractmethod
	def SetUniverseId(self, universeId: int) -> None:
		pass

	@abstractmethod
	def Shutdown(self) -> None:
		pass

	@abstractmethod
	def GetObjectsAsync(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def HttpGetAsync(self, url: str, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def HttpPostAsync(self, url: str, data: str, contentType: str, httpRequestType: HttpRequestType) -> str:
		pass

	@abstractmethod
	def InsertObjectsAndJoinIfLegacyAsync(self, url: Content) -> list[Instance]:
		pass

	@abstractmethod
	def SavePlace(self, saveFilter: SaveFilter) -> bool:
		pass


	pass

class GenericSettings(ServiceProvider):

	pass

class AnalysticsSettings(GenericSettings):

	pass

class GlobalSettings(GenericSettings):
	@abstractmethod
	def GetFFlag(self, name: str) -> bool:
		pass

	@abstractmethod
	def GetFVariable(self, name: str) -> str:
		pass


	pass

class UserSettings(GenericSettings):
	@abstractmethod
	def IsUserFeatureEnabled(self, name: str) -> bool:
		pass

	@abstractmethod
	def Reset(self) -> None:
		pass


	pass

class SessionService(Instance):
	@abstractmethod
	def GetCreatedTimestampUtcMs(self, sid: str) -> int:
		pass

	@abstractmethod
	def GetMetadata(self, sid: str, key: str) -> Any:
		pass

	@abstractmethod
	def GetRootSID(self) -> str:
		pass

	@abstractmethod
	def RemoveMetadata(self, sid: str, key: str) -> None:
		pass

	@abstractmethod
	def RemoveSession(self, sid: str) -> None:
		pass

	@abstractmethod
	def RemoveSessionsWithMetadataKey(self, key: str) -> None:
		pass

	@abstractmethod
	def ReplaceSession(self, sid: str, tag: str) -> None:
		pass

	@abstractmethod
	def SessionExists(self, sid: str) -> bool:
		pass

	@abstractmethod
	def SetMetadata(self, sid: str, key: str, value: Any) -> None:
		pass

	@abstractmethod
	def SetSession(self, parentSid: str, childSid: str, tag: str) -> None:
		pass


	pass

class Sky(Instance):
	CelestialBodiesShown: bool
	MoonAngularSize: float
	MoonTextureId: Content
	SkyboxBk: Content
	SkyboxDn: Content
	SkyboxFt: Content
	SkyboxLf: Content
	SkyboxRt: Content
	SkyboxUp: Content
	StarCount: int
	SunAngularSize: float
	SunTextureId: Content

	pass

class Smoke(Instance):
	Color: Color3
	Enabled: bool
	Opacity: float
	RiseVelocity: float
	Size: float
	TimeScale: float
	@abstractmethod
	def FastForward(self, numFrames: int) -> None:
		pass


	pass

class SnippetService(Instance):

	pass

class SocialService(Instance):
	@abstractmethod
	def InvokeGameInvitePromptClosed(self, player: Instance, recipientIds: list[Any]) -> None:
		pass

	@abstractmethod
	def PromptGameInvite(self, player: Instance) -> None:
		pass

	@abstractmethod
	def CanSendGameInviteAsync(self, player: Instance, recipientId: int) -> bool:
		pass


	pass

class Sound(Instance):
	ChannelCount: int
	EmitterSize: float
	IsLoaded: bool
	IsPaused: bool
	IsPlaying: bool
	LoopRegion: NumberRange
	Looped: bool
	MaxDistance: float
	MinDistance: float
	Pitch: float
	PlayOnRemove: bool
	PlaybackLoudness: float
	PlaybackRegion: NumberRange
	PlaybackRegionsEnabled: bool
	PlaybackSpeed: float
	Playing: bool
	RollOffMaxDistance: float
	RollOffMinDistance: float
	SoundGroup: 'SoundGroup'
	SoundId: Content
	TimeLength: float
	TimePosition: float
	UsageContextPermission: UsageContext
	Volume: float
	isPlaying: bool
	RollOffMode: RollOffMode
	@abstractmethod
	def Pause(self) -> None:
		pass

	@abstractmethod
	def Play(self) -> None:
		pass

	@abstractmethod
	def Resume(self) -> None:
		pass

	@abstractmethod
	def Stop(self) -> None:
		pass

	@abstractmethod
	def pause(self) -> None:
		pass

	@abstractmethod
	def play(self) -> None:
		pass

	@abstractmethod
	def stop(self) -> None:
		pass


	pass

class SoundEffect(Instance):
	Enabled: bool
	Priority: int

	pass

class AssetSoundEffect(SoundEffect):

	pass

class ChorusSoundEffect(SoundEffect):
	Depth: float
	Mix: float
	Rate: float

	pass

class CompressorSoundEffect(SoundEffect):
	Attack: float
	GainMakeup: float
	Ratio: float
	Release: float
	SideChain: Instance
	Threshold: float

	pass

class CustomSoundEffect(SoundEffect):

	pass

class ChannelSelectorSoundEffect(CustomSoundEffect):
	Channel: int

	pass

class DistortionSoundEffect(SoundEffect):
	Level: float

	pass

class EchoSoundEffect(SoundEffect):
	Delay: float
	DryLevel: float
	Feedback: float
	WetLevel: float

	pass

class EqualizerSoundEffect(SoundEffect):
	HighGain: float
	LowGain: float
	MidGain: float

	pass

class FlangeSoundEffect(SoundEffect):
	Depth: float
	Mix: float
	Rate: float

	pass

class PitchShiftSoundEffect(SoundEffect):
	Octave: float

	pass

class ReverbSoundEffect(SoundEffect):
	DecayTime: float
	Density: float
	Diffusion: float
	DryLevel: float
	WetLevel: float

	pass

class TremoloSoundEffect(SoundEffect):
	Depth: float
	Duty: float
	Frequency: float

	pass

class SoundGroup(Instance):
	Volume: float

	pass

class SoundService(Instance):
	AmbientReverb: ReverbType
	DistanceFactor: float
	DopplerScale: float
	RespectFilteringEnabled: bool
	RolloffScale: float
	VolumetricAudio: VolumetricAudio
	@abstractmethod
	def BeginRecording(self) -> bool:
		pass

	@abstractmethod
	def GetListener(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetOutputDevice(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetOutputDevices(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetSoundMemoryData(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def PlayLocalSound(self, sound: Instance) -> None:
		pass

	@abstractmethod
	def SetListener(self, listenerType: ListenerType, listener: tuple[Any]) -> None:
		pass

	@abstractmethod
	def SetOutputDevice(self, name: str, guid: str) -> None:
		pass

	@abstractmethod
	def SetRecordingDevice(self, deviceIndex: int) -> bool:
		pass

	@abstractmethod
	def EndRecording(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetRecordingDevices(self) -> dict[Any, Any]:
		pass


	pass

class Sparkles(Instance):
	Color: Color3
	Enabled: bool
	SparkleColor: Color3
	TimeScale: float
	@abstractmethod
	def FastForward(self, numFrames: int) -> None:
		pass


	pass

class SpawnerService(Instance):

	pass

class Speaker(Instance):
	ChannelCount: int
	PlaybackLoudness: float
	RollOffMaxDistance: float
	RollOffMinDistance: float
	Source: Instance
	Volume: float
	RollOffMode: RollOffMode
	SoundGroup: SoundGroup

	pass

class StackFrame(Instance):
	FrameId: int
	FrameName: str
	FrameType: DebuggerFrameType
	Globals: DebuggerVariable
	Line: int
	Locals: DebuggerVariable
	Populated: bool
	Script: str
	Upvalues: DebuggerVariable

	pass

class StandalonePluginScripts(Instance):

	pass

class StarterGear(Instance):

	pass

class StarterPack(Instance):

	pass

class StarterPlayer(Instance):
	AllowCustomAnimations: bool
	AutoJumpEnabled: bool
	CameraMaxZoomDistance: float
	CameraMinZoomDistance: float
	CharacterJumpHeight: float
	CharacterJumpPower: float
	CharacterMaxSlopeAngle: float
	CharacterUseJumpPower: bool
	CharacterWalkSpeed: float
	EnableDynamicHeads: LoadDynamicHeads
	EnableMouseLockOption: bool
	GameSettingsAssetIDFace: int
	GameSettingsAssetIDHead: int
	GameSettingsAssetIDLeftArm: int
	GameSettingsAssetIDLeftLeg: int
	GameSettingsAssetIDPants: int
	GameSettingsAssetIDRightArm: int
	GameSettingsAssetIDRightLeg: int
	GameSettingsAssetIDShirt: int
	GameSettingsAssetIDTeeShirt: int
	GameSettingsAssetIDTorso: int
	GameSettingsAvatar: GameAvatarType
	GameSettingsR15Collision: R15CollisionType
	GameSettingsScaleRangeBodyType: NumberRange
	GameSettingsScaleRangeHead: NumberRange
	GameSettingsScaleRangeHeight: NumberRange
	GameSettingsScaleRangeProportion: NumberRange
	GameSettingsScaleRangeWidth: NumberRange
	HealthDisplayDistance: float
	LoadCharacterAppearance: bool
	LoadCharacterLayeredClothing: LoadCharacterLayeredClothing
	NameDisplayDistance: float
	UserEmotesEnabled: bool
	CameraMode: CameraMode
	DevCameraOcclusionMode: DevCameraOcclusionMode
	DevComputerCameraMovementMode: DevComputerCameraMovementMode
	DevComputerMovementMode: DevComputerMovementMode
	DevTouchCameraMovementMode: DevTouchCameraMovementMode
	DevTouchMovementMode: DevTouchMovementMode
	HumanoidStateMachineMode: HumanoidStateMachineMode
	@abstractmethod
	def ClearDefaults(self) -> None:
		pass


	pass

class StarterPlayerScripts(Instance):

	pass

class StarterCharacterScripts(StarterPlayerScripts):

	pass

class Stats(Instance):
	ContactsCount: int
	DataReceiveKbps: float
	DataSendKbps: float
	HeartbeatTimeMs: float
	InstanceCount: int
	MovingPrimitivesCount: int
	PhysicsReceiveKbps: float
	PhysicsSendKbps: float
	PhysicsStepTimeMs: float
	PrimitivesCount: int
	@abstractmethod
	def GetBrowserTrackerId(self) -> str:
		pass

	@abstractmethod
	def GetMemoryUsageMbForTag(self, tag: DeveloperMemoryTag) -> float:
		pass

	@abstractmethod
	def GetTotalMemoryUsageMb(self) -> float:
		pass

	@abstractmethod
	def GetPaginatedMemoryByTexture(self, queryType: TextureQueryType, pageIndex: int, pageSize: int) -> dict[Any, Any]:
		pass


	pass

class StatsItem(Instance):
	DisplayName: str
	@abstractmethod
	def GetValue(self) -> float:
		pass

	@abstractmethod
	def GetValueString(self) -> str:
		pass


	pass

class RunningAverageItemDouble(StatsItem):

	pass

class RunningAverageItemInt(StatsItem):

	pass

class RunningAverageTimeIntervalItem(StatsItem):

	pass

class TotalCountTimeIntervalItem(StatsItem):

	pass

class StopWatchReporter(Instance):
	@abstractmethod
	def FinishTask(self, taskId: int) -> None:
		pass

	@abstractmethod
	def SendReport(self, reportName: str) -> None:
		pass

	@abstractmethod
	def StartTask(self, reportName: str, taskName: str) -> int:
		pass


	pass

class Studio(Instance):
	TODOColor: Color3
	functionColor: Color3
	localColor: Color3
	nilColor: Color3
	selfColor: Color3
	ActiveColor: Color3
	ActiveHoverOverColor: Color3
	AlwaysSaveScriptChanges: bool
	AnimateHoverOver: bool
	AutoCleanEmptyLine: bool
	AutoClosingBrackets: bool
	AutoClosingQuotes: bool
	AutoIndentRule: AutoIndentRule
	AutoRecoveryEnabled: bool
	AutoRecoveryIntervalMinutes: int
	AutoRecoveryPath: QDir
	BackgroundColor: Color3
	BasicObjectsDisplayMode: ListDisplayMode
	BoolColor: Color3
	BracketColor: Color3
	BuiltinFunctionColor: Color3
	CameraMouseWheelSpeed: float
	CameraPanSpeed: float
	CameraShiftSpeed: float
	CameraSpeed: float
	CameraZoomtoMousePosition: bool
	ClearOutputOnStart: bool
	CommandBarLocalState: bool
	CommentColor: Color3
	CurrentLineHighlightColor: Color3
	DebuggerCurrentLineColor: Color3
	DebuggerErrorLineColor: Color3
	DefaultScriptFileDir: QDir
	DeprecatedObjectsShown: bool
	DisplayLanguage: str
	DocViewCodeBackgroundColor: Color3
	DragMultiplePartsAsSinglePart: bool
	EnableAutocomplete: bool
	EnableAutocompleteDocView: bool
	EnableCoreScriptDebugger: bool
	EnableHttpSandboxing: bool
	EnableInternalBetaFeatures: bool
	EnableInternalFeatures: bool
	EnableScriptAnalysis: bool
	EnableScrollbarMarkers: bool
	EnableSignatureHelp: bool
	EnableSignatureHelpDocView: bool
	EnableTemporaryTabs: bool
	EnableTemporaryTabsInExplorer: bool
	EnableTypeHover: bool
	EnableOnTypeAutocomplete: bool
	ErrorColor: Color3
	FileNewcreatesaplacewithTeamCreateoff: bool
	FindSelectionBackgroundColor: Color3
	Font: QFont
	FormatOnPaste: bool
	FormatOnType: bool
	FunctionNameColor: Color3
	HighlightCurrentLine: bool
	HighlightOccurances: bool
	HoverAnimateSpeed: HoverAnimateSpeed
	HoverBoxThickness: float
	HoverLineThickness: int
	HoverOverColor: Color3
	IconOverrideDir: QDir
	IndentUsingSpaces: bool
	KeywordColor: Color3
	LineThickness: float
	LocalAssetsFolder: QDir
	LuaDebuggerEnabled: bool
	LuaDebuggerEnabledAtStartup: bool
	LuauKeywordColor: Color3
	MainVolume: float
	MatchingWordBackgroundColor: Color3
	MaximumOutputLines: int
	MenuItemBackgroundColor: Color3
	MethodColor: Color3
	NumberColor: Color3
	OnlyPlayAudiofromWindowinFocus: bool
	OperatorColor: Color3
	OutputFont: QFont
	OutputLayoutMode: OutputLayoutMode
	PhysicalDraggersSelectScopeByDefault: bool
	PivotSnapToGeometryColor: Color3
	PluginDebuggingEnabled: bool
	PluginsDir: QDir
	PrimaryTextColor: Color3
	PropertyColor: Color3
	RenderThrottlePercentage: int
	RespectStudioshortcutswhengamehasfocus: bool
	RulerColor: Color3
	Rulers: str
	ScriptEditorColorPreset: StudioScriptEditorColorPresets
	ScriptEditorScrollbarBackgroundColor: Color3
	ScriptEditorScrollbarHandleColor: Color3
	ScriptEditorMenuBorderColor: Color3
	ScriptEditorShouldShowPluginMethods: bool
	ScriptTimeoutLength: int
	ScrollPastLastLine: bool
	SearchContentForCoreScripts: bool
	SecondaryTextColor: Color3
	SelectColor: Color3
	SelectHoverColor: Color3
	SelectedMenuItemBackgroundColor: Color3
	SelectedTextColor: Color3
	SelectionBackgroundColor: Color3
	SelectionColor: Color3
	SelectionHighlightThickness: float
	SelectionLineThickness: int
	ServerAudioBehavior: ServerAudioBehavior
	SetPivotofImportedParts: bool
	ShowCoreGUIinExplorerwhilePlaying: bool
	ShowDeploymentWarnings: bool
	ShowDiagnosticsBar: bool
	ShowFileSyncService: bool
	ShowHiddenObjectsinExplorer: bool
	ShowHoverOver: bool
	ShowLightGuides: bool
	ShowNavigationLabels: bool
	ShowNavigationMesh: bool
	ShowPathfindingLinks: bool
	ShowPluginGUIServiceinExplorer: bool
	ShowQTwarningsinoutput: bool
	ShowWhitespace: bool
	ShowplusbuttononhoverinExplorer: bool
	ShowCorePackagesInExplorer: bool
	SkipClosingBracketsandQuotes: bool
	StringColor: Color3
	TabWidth: int
	TextColor: Color3
	TextWrapping: bool
	Theme: Instance
	UITheme: UITheme
	UseBoundingBoxMoveHandles: bool
	WarningColor: Color3
	WhitespaceColor: Color3
	PermissionLevelShown: PermissionLevelShown
	RuntimeUndoBehavior: RuntimeUndoBehavior
	@abstractmethod
	def GetAvailableThemes(self) -> list[Any]:
		pass


	pass

class StudioAssetService(Instance):
	@abstractmethod
	def ConvertToPackageUpload(self, uploadUrl: str, cloneInstances: list[Instance], originalInstances: list[Instance]) -> None:
		pass

	@abstractmethod
	def SerializeInstances(self, instances: list[Instance]) -> str:
		pass


	pass

class StudioData(Instance):
	EnableScriptCollabByDefaultOnLoad: bool
	SrcPlaceId: int
	SrcUniverseId: int

	pass

class StudioDeviceEmulatorService(Instance):
	HasMultiTouchStarted: bool
	IsMultiTouchEmulationOn: bool
	IsMultiTouchEnabled: bool
	PivotPosition: Vector2
	@abstractmethod
	def GetMaxNumTouches(self) -> int:
		pass

	@abstractmethod
	def GetTouchInBounds(self, index: int) -> bool:
		pass

	@abstractmethod
	def GetTouchPosition(self, index: int) -> Vector2:
		pass

	@abstractmethod
	def EmulatePCDeviceWithResolution(self, deviceId: str, resolution: Vector2) -> bool:
		pass

	@abstractmethod
	def GetCurrentDeviceId(self) -> str:
		pass

	@abstractmethod
	def GetCurrentOrientation(self) -> ScreenOrientation:
		pass

	@abstractmethod
	def HasDeviceWithId(self, deviceId: str) -> bool:
		pass

	@abstractmethod
	def SetCurrentDeviceId(self, deviceId: str) -> None:
		pass

	@abstractmethod
	def SetCurrentOrientation(self, orientation: ScreenOrientation) -> None:
		pass


	pass

class StudioHighDpiService(Instance):
	@abstractmethod
	def IsNotHighDPIAwareBuild(self) -> bool:
		pass


	pass

class StudioPublishService(Instance):
	@abstractmethod
	def ClearUploadNames(self) -> None:
		pass

	@abstractmethod
	def PublishAs(self, universeId: int, placeId: int, groupId: int, isPublish: bool, publishParameters: Any) -> None:
		pass

	@abstractmethod
	def PublishThenTurnOnTeamCreate(self) -> None:
		pass

	@abstractmethod
	def RefreshDocumentDisplayName(self) -> None:
		pass

	@abstractmethod
	def SetTeamCreateOnPublishInfo(self, shouldTurnOnTcOnPublish: bool, newPlaceName: str) -> None:
		pass

	@abstractmethod
	def SetUniverseDisplayName(self, newName: str) -> None:
		pass

	@abstractmethod
	def SetUploadNames(self, placeName: str, universeName: str) -> None:
		pass

	@abstractmethod
	def ShowSaveOrPublishPlaceToRoblox(self, showGameSelect: bool, isPublish: bool, closeMode: StudioCloseMode) -> None:
		pass


	pass

class StudioScriptDebugEventListener(Instance):

	pass

class StudioService(Instance):
	ActiveScript: Instance
	AlignDraggedObjects: bool
	DraggerSolveConstraints: bool
	DrawConstraintsOnTop: bool
	GridSize: float
	HoverInstance: Instance
	InstalledPluginData: str
	PivotSnapToGeometry: bool
	RotateIncrement: float
	ShowActiveInstanceHighlight: bool
	ShowConstraintDetails: bool
	StudioLocaleId: str
	UseLocalSpace: bool
	@abstractmethod
	def AnimationIdSelected(self, id: int) -> None:
		pass

	@abstractmethod
	def CopyToClipboard(self, stringToCopy: str) -> None:
		pass

	@abstractmethod
	def GetBadgeConfigureUrl(self, badgeId: int) -> str:
		pass

	@abstractmethod
	def GetBadgeUploadUrl(self) -> str:
		pass

	@abstractmethod
	def GetClassIcon(self, className: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetPlaceIsPersistedToCloud(self) -> bool:
		pass

	@abstractmethod
	def GetResourceByCategory(self, category: str) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetStartupAssetId(self) -> str:
		pass

	@abstractmethod
	def GetStartupPluginId(self) -> str:
		pass

	@abstractmethod
	def GetTermsOfUseUrl(self) -> str:
		pass

	@abstractmethod
	def GetUserId(self) -> int:
		pass

	@abstractmethod
	def GizmoRaycast(self, origin: Vector3, direction: Vector3, raycastParams: 'RaycastParams') -> 'RaycastResult':
		pass

	@abstractmethod
	def HasInternalPermission(self) -> bool:
		pass

	@abstractmethod
	def IsPluginInstalled(self, assetId: int) -> bool:
		pass

	@abstractmethod
	def IsPluginUpToDate(self, assetId: int, currentAssetVersion: int) -> bool:
		pass

	@abstractmethod
	def OpenInBrowser_DONOTUSE(self, url: str) -> None:
		pass

	@abstractmethod
	def RequestClose(self, closeMode: StudioCloseMode) -> None:
		pass

	@abstractmethod
	def SetPluginEnabled(self, assetId: int, state: bool) -> None:
		pass

	@abstractmethod
	def ShowPlaceVersionHistoryDialog(self, placeId: int) -> None:
		pass

	@abstractmethod
	def ShowPublishToRoblox(self) -> None:
		pass

	@abstractmethod
	def UninstallPlugin(self, assetId: int) -> None:
		pass

	@abstractmethod
	def UpdatePluginManagement(self) -> None:
		pass

	@abstractmethod
	def PromptImportFile(self, fileTypeFilter: list[Any]) -> Instance:
		pass

	@abstractmethod
	def PromptImportFiles(self, fileTypeFilter: list[Any]) -> list[Instance]:
		pass

	@abstractmethod
	def TryInstallPlugin(self, assetId: int, assetVersionId: int) -> None:
		pass


	pass

class StudioTheme(Instance):
	@abstractmethod
	def GetColor(self, styleguideitem: StudioStyleGuideColor, modifier: StudioStyleGuideModifier) -> Color3:
		pass


	pass

class SurfaceAppearance(Instance):
	ColorMap: Content
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	TexturePack: Content
	AlphaMode: AlphaMode

	pass

class TaskScheduler(Instance):
	SchedulerDutyCycle: float
	SchedulerRate: float
	ThreadPoolSize: int
	ThreadPoolConfig: ThreadPoolConfig

	pass

class Team(Instance):
	AutoAssignable: bool
	AutoColorCharacters: bool
	ChildOrder: int
	Score: int
	TeamColor: BrickColor
	@abstractmethod
	def GetPlayers(self) -> list[Instance]:
		pass


	pass

class TeamCreateService(Instance):
	@abstractmethod
	def SendUnarchiveUniverseAsync(self, universeId: int) -> None:
		pass


	pass

class Teams(Instance):
	@abstractmethod
	def GetTeams(self) -> list[Instance]:
		pass

	@abstractmethod
	def RebalanceTeams(self) -> None:
		pass


	pass

class TeleportAsyncResult(Instance):
	PrivateServerId: str
	ReservedServerAccessCode: str

	pass

class TeleportOptions(Instance):
	ReservedServerAccessCode: str
	ServerInstanceId: str
	ShouldReserveServer: bool
	@abstractmethod
	def GetTeleportData(self) -> Any:
		pass

	@abstractmethod
	def SetTeleportData(self, teleportData: Any) -> None:
		pass


	pass

class TeleportService(Instance):
	CustomizedTeleportUI: bool
	@abstractmethod
	def Block(self) -> None:
		pass

	@abstractmethod
	def GetArrivingTeleportGui(self) -> Instance:
		pass

	@abstractmethod
	def GetLocalPlayerTeleportData(self) -> Any:
		pass

	@abstractmethod
	def GetTeleportSetting(self, setting: str) -> Any:
		pass

	@abstractmethod
	def SetTeleportGui(self, gui: Instance) -> None:
		pass

	@abstractmethod
	def SetTeleportSetting(self, setting: str, value: Any) -> None:
		pass

	@abstractmethod
	def Teleport(self, placeId: int, player: Instance, teleportData: Any, customLoadingScreen: Instance) -> None:
		pass

	@abstractmethod
	def TeleportCancel(self) -> None:
		pass

	@abstractmethod
	def TeleportToPlaceInstance(self, placeId: int, instanceId: str, player: Instance, spawnName: str, teleportData: Any, customLoadingScreen: Instance) -> None:
		pass

	@abstractmethod
	def TeleportToPrivateServer(self, placeId: int, reservedServerAccessCode: str, players: list[Instance], spawnName: str, teleportData: Any, customLoadingScreen: Instance) -> None:
		pass

	@abstractmethod
	def TeleportToSpawnByName(self, placeId: int, spawnName: str, player: Instance, teleportData: Any, customLoadingScreen: Instance) -> None:
		pass

	@abstractmethod
	def GetPlayerPlaceInstanceAsync(self, userId: int) -> tuple[Any]:
		pass

	@abstractmethod
	def ReserveServer(self, placeId: int) -> tuple[Any]:
		pass

	@abstractmethod
	def TeleportAsync(self, placeId: int, players: list[Instance], teleportOptions: Instance) -> Instance:
		pass

	@abstractmethod
	def TeleportPartyAsync(self, placeId: int, players: list[Instance], teleportData: Any, customLoadingScreen: Instance) -> str:
		pass

	@abstractmethod
	def UnblockAsync(self) -> tuple[Any]:
		pass


	pass

class TemporaryCageMeshProvider(Instance):

	pass

class TemporaryScriptService(Instance):

	pass

class TerrainDetail(Instance):
	ColorMap: Content
	Face: TerrainFace
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	StudsPerTile: float
	MaterialPattern: MaterialPattern

	pass

class TerrainRegion(Instance):
	IsSmooth: bool
	SizeInCells: Vector3
	@abstractmethod
	def ConvertToSmooth(self) -> None:
		pass


	pass

class TestService(Instance):
	AutoRuns: bool
	Description: str
	ErrorCount: int
	ExecuteWithStudioRun: bool
	Is30FpsThrottleEnabled: bool
	IsPhysicsEnvironmentalThrottled: bool
	IsSleepAllowed: bool
	NumberOfPlayers: int
	SimulateSecondsLag: float
	TestCount: int
	Timeout: float
	WarnCount: int
	@abstractmethod
	def Check(self, condition: bool, description: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def Checkpoint(self, text: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def Done(self) -> None:
		pass

	@abstractmethod
	def Error(self, description: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def Fail(self, description: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def Message(self, text: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def Require(self, condition: bool, description: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def ScopeTime(self) -> dict[Any, Any]:
		pass

	@abstractmethod
	def Warn(self, condition: bool, description: str, source: Instance, line: int) -> None:
		pass

	@abstractmethod
	def isFeatureEnabled(self, name: str) -> bool:
		pass

	@abstractmethod
	def Run(self) -> None:
		pass


	pass

class TextBoxService(Instance):

	pass

class TextChannel(Instance):
	@abstractmethod
	def DisplaySystemMessage(self, systemMessage: str, metadata: str) -> 'TextChatMessage':
		pass

	@abstractmethod
	def AddUserAsync(self, userId: int) -> tuple[Any]:
		pass

	@abstractmethod
	def SendAsync(self, message: str, metadata: str) -> 'TextChatMessage':
		pass


	pass

class TextChatCommand(Instance):
	Enabled: bool
	PrimaryAlias: str
	SecondaryAlias: str

	pass

class TextChatConfigurations(Instance):

	pass

class BubbleChatConfiguration(TextChatConfigurations):
	AdorneeName: str
	BackgroundColor3: Color3
	BubbleDuration: float
	BubblesSpacing: float
	Enabled: bool
	LocalPlayerStudsOffset: Vector3
	MaxDistance: float
	MinimizeDistance: float
	TextColor3: Color3
	TextSize: int
	VerticalStudsOffset: float
	Font: Font

	pass

class ChatInputBarConfiguration(TextChatConfigurations):
	AbsolutePosition: Vector2
	AbsolutePositionWrite: Vector2
	AbsoluteSize: Vector2
	AbsoluteSizeWrite: Vector2
	Enabled: bool
	TargetTextChannel: TextChannel

	pass

class ChatWindowConfiguration(TextChatConfigurations):
	AbsolutePosition: Vector2
	AbsolutePositionWrite: Vector2
	AbsoluteSize: Vector2
	AbsoluteSizeWrite: Vector2
	Enabled: bool
	HorizontalAlignment: HorizontalAlignment
	VerticalAlignment: VerticalAlignment

	pass

class TextChatMessage(Instance):
	MessageId: str
	Metadata: str
	PrefixText: str
	Status: TextChatMessageStatus
	Text: str
	TextSource: 'TextSource'
	Timestamp: DateTime
	TextChannel: TextChannel

	pass

class TextChatMessageProperties(Instance):
	PrefixText: str
	Text: str

	pass

class TextChatService(Instance):
	CreateDefaultCommands: bool
	CreateDefaultTextChannels: bool
	ChatVersion: ChatVersion

	pass

class TextFilterResult(Instance):
	@abstractmethod
	def GetChatForUserAsync(self, toUserId: int) -> str:
		pass

	@abstractmethod
	def GetNonChatStringForBroadcastAsync(self) -> str:
		pass

	@abstractmethod
	def GetNonChatStringForUserAsync(self, toUserId: int) -> str:
		pass


	pass

class TextService(Instance):
	@abstractmethod
	def GetTextSize(self, string: str, fontSize: int, font: Font, frameSize: Vector2) -> Vector2:
		pass

	@abstractmethod
	def SetResolutionScale(self, scale: float) -> None:
		pass

	@abstractmethod
	def FilterStringAsync(self, stringToFilter: str, fromUserId: int, textContext: TextFilterContext) -> Instance:
		pass

	@abstractmethod
	def GetFamilyInfoAsync(self, assetId: Content) -> dict[Any, Any]:
		pass

	@abstractmethod
	def GetTextBoundsAsync(self, params: GetTextBoundsParams) -> Vector2:
		pass


	pass

class TextSource(Instance):
	CanSend: bool
	UserId: int

	pass

class ThirdPartyUserService(Instance):
	@abstractmethod
	def GetUserPlatformId(self) -> str:
		pass

	@abstractmethod
	def GetUserPlatformName(self) -> str:
		pass

	@abstractmethod
	def HaveActiveUser(self) -> bool:
		pass

	@abstractmethod
	def ReturnToEngagement(self) -> None:
		pass

	@abstractmethod
	def ShowAccountPicker(self) -> None:
		pass

	@abstractmethod
	def RegisterActiveUser(self, gamepadId: UserInputType) -> int:
		pass


	pass

class ThreadState(Instance):
	FrameCount: int
	Populated: bool
	ThreadId: int
	ThreadName: str
	@abstractmethod
	def GetFrame(self, index: int) -> Instance:
		pass


	pass

class TimerService(Instance):

	pass

class ToastNotificationService(Instance):
	@abstractmethod
	def HideNotification(self, notificationId: str) -> None:
		pass

	@abstractmethod
	def ShowNotification(self, message: str, notificationId: str) -> None:
		pass


	pass

class TouchInputService(Instance):

	pass

class TouchTransmitter(Instance):

	pass

class TracerService(Instance):
	@abstractmethod
	def FinishSpan(self, spanId: str) -> None:
		pass

	@abstractmethod
	def StartSpan(self, name: str, parentId: str) -> str:
		pass


	pass

class TrackerLodController(Instance):
	AudioMode: TrackerLodFlagMode
	VideoExtrapolationMode: TrackerExtrapolationFlagMode
	VideoLodMode: TrackerLodValueMode
	VideoMode: TrackerLodFlagMode
	@abstractmethod
	def getExtrapolation(self) -> int:
		pass

	@abstractmethod
	def getVideoLod(self) -> int:
		pass

	@abstractmethod
	def isAudioEnabled(self) -> bool:
		pass

	@abstractmethod
	def isVideoEnabled(self) -> bool:
		pass


	pass

class TrackerStreamAnimation(Instance):

	pass

class Trail(Instance):
	Attachment0: Attachment
	Attachment1: Attachment
	Brightness: float
	Color: ColorSequence
	Enabled: bool
	FaceCamera: bool
	Lifetime: float
	LightEmission: float
	LightInfluence: float
	MaxLength: float
	MinLength: float
	Texture: Content
	TextureLength: float
	Transparency: NumberSequence
	WidthScale: NumberSequence
	TextureMode: TextureMode
	@abstractmethod
	def Clear(self) -> None:
		pass


	pass

class Translator(Instance):
	LocaleId: str
	@abstractmethod
	def FormatByKey(self, key: str, args: Any) -> str:
		pass

	@abstractmethod
	def RobloxOnlyTranslate(self, context: Instance, text: str) -> str:
		pass

	@abstractmethod
	def Translate(self, context: Instance, text: str) -> str:
		pass


	pass

class TweenBase(Instance):
	PlaybackState: PlaybackState
	@abstractmethod
	def Cancel(self) -> None:
		pass

	@abstractmethod
	def Pause(self) -> None:
		pass

	@abstractmethod
	def Play(self) -> None:
		pass


	pass

class Tween(TweenBase):
	Instance: Instance
	TweenInfo: TweenInfo

	pass

class TweenService(Instance):
	@abstractmethod
	def Create(self, instance: Instance, tweenInfo: TweenInfo, propertyTable: dict[Any, Any]) -> Tween:
		pass

	@abstractmethod
	def GetValue(self, alpha: float, easingStyle: EasingStyle, easingDirection: EasingDirection) -> float:
		pass


	pass

class UGCValidationService(Instance):
	@abstractmethod
	def GetMeshTriCountSync(self, meshId: str) -> int:
		pass

	@abstractmethod
	def GetMeshVertsSync(self, meshId: str) -> list[Any]:
		pass

	@abstractmethod
	def GetTextureSizeSync(self, textureId: str) -> Vector2:
		pass

	@abstractmethod
	def ResetCollisionFidelity(self, meshPart: Instance) -> None:
		pass

	@abstractmethod
	def SetMeshIdBlocking(self, meshPart: Instance, meshId: str) -> None:
		pass

	@abstractmethod
	def FetchAssetWithFormat(self, url: Content, assetFormat: str) -> list[Instance]:
		pass

	@abstractmethod
	def GetMeshTriCount(self, meshId: str) -> int:
		pass

	@abstractmethod
	def GetMeshVertColors(self, meshId: str) -> list[Any]:
		pass

	@abstractmethod
	def GetMeshVerts(self, meshId: str) -> list[Any]:
		pass

	@abstractmethod
	def GetTextureSize(self, textureId: str) -> Vector2:
		pass

	@abstractmethod
	def ValidateCageMeshIntersection(self, innerCageMeshId: str, outerCageMeshId: str, refMeshId: str) -> tuple[Any]:
		pass

	@abstractmethod
	def ValidateCageNonManifoldAndHoles(self, meshId: str) -> tuple[Any]:
		pass

	@abstractmethod
	def ValidateFullBodyCageDeletion(self, meshId: str) -> bool:
		pass

	@abstractmethod
	def ValidateMeshTriangles(self, meshId: str) -> bool:
		pass

	@abstractmethod
	def ValidateMeshVertColors(self, meshId: str) -> bool:
		pass

	@abstractmethod
	def ValidateMisMatchUV(self, innerCageMeshId: str, outerCageMeshId: str) -> bool:
		pass

	@abstractmethod
	def ValidateOverlappingVertices(self, meshId: str) -> bool:
		pass

	@abstractmethod
	def ValidateTextureSize(self, textureId: str) -> bool:
		pass

	@abstractmethod
	def ValidateUVSpace(self, meshId: str) -> bool:
		pass


	pass

class UIBase(Instance):

	pass

class UIComponent(UIBase):

	pass

class UIConstraint(UIComponent):

	pass

class UIAspectRatioConstraint(UIConstraint):
	AspectRatio: float
	AspectType: AspectType
	DominantAxis: DominantAxis

	pass

class UISizeConstraint(UIConstraint):
	MaxSize: Vector2
	MinSize: Vector2

	pass

class UITextSizeConstraint(UIConstraint):
	MaxTextSize: int
	MinTextSize: int

	pass

class UICorner(UIComponent):
	CornerRadius: UDim

	pass

class UIGradient(UIComponent):
	Color: ColorSequence
	Enabled: bool
	Offset: Vector2
	Rotation: float
	Transparency: NumberSequence

	pass

class UILayout(UIComponent):

	pass

class UIGridStyleLayout(UILayout):
	AbsoluteContentSize: Vector2
	FillDirection: FillDirection
	HorizontalAlignment: HorizontalAlignment
	SortOrder: SortOrder
	VerticalAlignment: VerticalAlignment
	@abstractmethod
	def ApplyLayout(self) -> None:
		pass

	@abstractmethod
	def SetCustomSortFunction(self, function: Callable[..., Any]) -> None:
		pass


	pass

class UIGridLayout(UIGridStyleLayout):
	AbsoluteCellCount: Vector2
	AbsoluteCellSize: Vector2
	CellPadding: UDim2
	CellSize: UDim2
	FillDirectionMaxCells: int
	StartCorner: StartCorner

	pass

class UIListLayout(UIGridStyleLayout):
	Padding: UDim

	pass

class UIPageLayout(UIGridStyleLayout):
	Animated: bool
	Circular: bool
	CurrentPage: GuiObject
	GamepadInputEnabled: bool
	Padding: UDim
	ScrollWheelInputEnabled: bool
	TouchInputEnabled: bool
	TweenTime: float
	EasingDirection: EasingDirection
	EasingStyle: EasingStyle
	@abstractmethod
	def JumpTo(self, page: Instance) -> None:
		pass

	@abstractmethod
	def JumpToIndex(self, index: int) -> None:
		pass

	@abstractmethod
	def Next(self) -> None:
		pass

	@abstractmethod
	def Previous(self) -> None:
		pass


	pass

class UITableLayout(UIGridStyleLayout):
	FillEmptySpaceColumns: bool
	FillEmptySpaceRows: bool
	MajorAxis: TableMajorAxis
	Padding: UDim2

	pass

class UIPadding(UIComponent):
	PaddingBottom: UDim
	PaddingLeft: UDim
	PaddingRight: UDim
	PaddingTop: UDim

	pass

class UIScale(UIComponent):
	Scale: float

	pass

class UIStroke(UIComponent):
	Color: Color3
	Enabled: bool
	Thickness: float
	Transparency: float
	ApplyStrokeMode: ApplyStrokeMode
	LineJoinMode: LineJoinMode

	pass

class UnvalidatedAssetService(Instance):
	@abstractmethod
	def AppendTempAssetId(self, userId: int, id: int, lookAt: Vector3, camPos: Vector3, usage: str) -> None:
		pass

	@abstractmethod
	def AppendVantagePoint(self, userId: int, id: int, lookAt: Vector3, camPos: Vector3) -> bool:
		pass

	@abstractmethod
	def UpgradeTempAssetId(self, userId: int, tempId: int, assetId: int) -> bool:
		pass


	pass

class UserGameSettings(Instance):
	AllTutorialsDisabled: bool
	CameraMode: CustomCameraMode
	CameraYInverted: bool
	ChatVisible: bool
	DefaultCameraID: str
	Fullscreen: bool
	GamepadCameraSensitivity: float
	GraphicsQualityLevel: int
	HasEverUsedVR: bool
	IsUsingCameraYInverted: bool
	IsUsingGamepadCameraSensitivity: bool
	MasterVolume: float
	MicroProfilerWebServerEnabled: bool
	MicroProfilerWebServerIP: str
	MicroProfilerWebServerPort: int
	MouseSensitivity: float
	MouseSensitivityFirstPerson: Vector2
	MouseSensitivityThirdPerson: Vector2
	OnScreenProfilerEnabled: bool
	OnboardingsCompleted: str
	PerformanceStatsVisible: bool
	RCCProfilerRecordFrameRate: int
	RCCProfilerRecordTimeFrame: int
	SavedQualityLevel: SavedQualitySetting
	StartMaximized: bool
	StartScreenPosition: Vector2
	StartScreenSize: Vector2
	UsedCoreGuiIsVisibleToggle: bool
	UsedCustomGuiIsVisibleToggle: bool
	UsedHideHudShortcut: bool
	VREnabled: bool
	VRRotationIntensity: int
	VRSmoothRotationEnabled: bool
	VignetteEnabled: bool
	ComputerCameraMovementMode: ComputerCameraMovementMode
	ComputerMovementMode: ComputerMovementMode
	ControlMode: ControlMode
	RotationType: RotationType
	TouchCameraMovementMode: TouchCameraMovementMode
	TouchMovementMode: TouchMovementMode
	@abstractmethod
	def GetCameraYInvertValue(self) -> int:
		pass

	@abstractmethod
	def GetOnboardingCompleted(self, onboardingId: str) -> bool:
		pass

	@abstractmethod
	def GetTutorialState(self, tutorialId: str) -> bool:
		pass

	@abstractmethod
	def InFullScreen(self) -> bool:
		pass

	@abstractmethod
	def InStudioMode(self) -> bool:
		pass

	@abstractmethod
	def ResetOnboardingCompleted(self, onboardingId: str) -> None:
		pass

	@abstractmethod
	def SetCameraYInvertVisible(self) -> None:
		pass

	@abstractmethod
	def SetGamepadCameraSensitivityVisible(self) -> None:
		pass

	@abstractmethod
	def SetOnboardingCompleted(self, onboardingId: str) -> None:
		pass

	@abstractmethod
	def SetTutorialState(self, tutorialId: str, value: bool) -> None:
		pass


	pass

class UserInputService(Instance):
	AccelerometerEnabled: bool
	BottomBarSize: Vector2
	GamepadEnabled: bool
	GazeSelectionEnabled: bool
	GyroscopeEnabled: bool
	KeyboardEnabled: bool
	LegacyInputEventsEnabled: bool
	ModalEnabled: bool
	MouseDeltaSensitivity: float
	MouseEnabled: bool
	MouseIconEnabled: bool
	NavBarSize: Vector2
	OnScreenKeyboardAnimationDuration: float
	OnScreenKeyboardPosition: Vector2
	OnScreenKeyboardSize: Vector2
	OnScreenKeyboardVisible: bool
	RightBarSize: Vector2
	StatusBarSize: Vector2
	TouchEnabled: bool
	UserHeadCFrame: CFrame
	VREnabled: bool
	MouseBehavior: MouseBehavior
	OverrideMouseIconBehavior: OverrideMouseIconBehavior
	@abstractmethod
	def GamepadSupports(self, gamepadNum: UserInputType, gamepadKeyCode: KeyCode) -> bool:
		pass

	@abstractmethod
	def GetConnectedGamepads(self) -> list[Any]:
		pass

	@abstractmethod
	def GetDeviceAcceleration(self) -> InputObject:
		pass

	@abstractmethod
	def GetDeviceGravity(self) -> InputObject:
		pass

	@abstractmethod
	def GetDeviceRotation(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetDeviceType(self) -> DeviceType:
		pass

	@abstractmethod
	def GetFocusedTextBox(self) -> TextBox:
		pass

	@abstractmethod
	def GetGamepadConnected(self, gamepadNum: UserInputType) -> bool:
		pass

	@abstractmethod
	def GetGamepadState(self, gamepadNum: UserInputType) -> list[Any]:
		pass

	@abstractmethod
	def GetKeysPressed(self) -> list[Any]:
		pass

	@abstractmethod
	def GetLastInputType(self) -> UserInputType:
		pass

	@abstractmethod
	def GetMouseButtonsPressed(self) -> list[Any]:
		pass

	@abstractmethod
	def GetMouseDelta(self) -> Vector2:
		pass

	@abstractmethod
	def GetMouseLocation(self) -> Vector2:
		pass

	@abstractmethod
	def GetNavigationGamepads(self) -> list[Any]:
		pass

	@abstractmethod
	def GetPlatform(self) -> Platform:
		pass

	@abstractmethod
	def GetStringForKeyCode(self, keyCode: KeyCode) -> str:
		pass

	@abstractmethod
	def GetSupportedGamepadKeyCodes(self, gamepadNum: UserInputType) -> list[Any]:
		pass

	@abstractmethod
	def GetUserCFrame(self, type: UserCFrame) -> CFrame:
		pass

	@abstractmethod
	def IsGamepadButtonDown(self, gamepadNum: UserInputType, gamepadKeyCode: KeyCode) -> bool:
		pass

	@abstractmethod
	def IsKeyDown(self, keyCode: KeyCode) -> bool:
		pass

	@abstractmethod
	def IsMouseButtonPressed(self, mouseButton: UserInputType) -> bool:
		pass

	@abstractmethod
	def IsNavigationGamepad(self, gamepadEnum: UserInputType) -> bool:
		pass

	@abstractmethod
	def RecenterUserHeadCFrame(self) -> None:
		pass

	@abstractmethod
	def SendAppUISizes(self, statusBarSize: Vector2, navBarSize: Vector2, bottomBarSize: Vector2, rightBarSize: Vector2) -> None:
		pass

	@abstractmethod
	def SetNavigationGamepad(self, gamepadEnum: UserInputType, enabled: bool) -> None:
		pass


	pass

class UserService(Instance):
	@abstractmethod
	def GetUserInfosByUserIdsAsync(self, userIds: list[Any]) -> list[Any]:
		pass


	pass

class VRService(Instance):
	DidPointerHit: bool
	GuiInputUserCFrame: UserCFrame
	LaserDistance: float
	PointerHitCFrame: CFrame
	VRDeviceAvailable: bool
	VRDeviceName: str
	VREnabled: bool
	@abstractmethod
	def GetTouchpadMode(self, pad: VRTouchpad) -> VRTouchpadMode:
		pass

	@abstractmethod
	def GetUserCFrame(self, type: UserCFrame) -> CFrame:
		pass

	@abstractmethod
	def GetUserCFrameEnabled(self, type: UserCFrame) -> bool:
		pass

	@abstractmethod
	def IsMaquettes(self) -> bool:
		pass

	@abstractmethod
	def IsVRAppBuild(self) -> bool:
		pass

	@abstractmethod
	def RecenterUserHeadCFrame(self) -> None:
		pass

	@abstractmethod
	def RequestNavigation(self, cframe: CFrame, inputUserCFrame: UserCFrame) -> None:
		pass

	@abstractmethod
	def SetTouchpadMode(self, pad: VRTouchpad, mode: VRTouchpadMode) -> None:
		pass


	pass

class ValueBase(Instance):

	pass

class BinaryStringValue(ValueBase):

	pass

class BoolValue(ValueBase):
	Value: bool

	pass

class BrickColorValue(ValueBase):
	Value: BrickColor

	pass

class CFrameValue(ValueBase):
	Value: CFrame

	pass

class Color3Value(ValueBase):
	Value: Color3

	pass

class DoubleConstrainedValue(ValueBase):
	ConstrainedValue: float
	MaxValue: float
	MinValue: float
	Value: float

	pass

class IntConstrainedValue(ValueBase):
	ConstrainedValue: int
	MaxValue: int
	MinValue: int
	Value: int

	pass

class IntValue(ValueBase):
	Value: int

	pass

class NumberValue(ValueBase):
	Value: float

	pass

class ObjectValue(ValueBase):
	Value: Instance

	pass

class RayValue(ValueBase):
	Value: Ray

	pass

class StringValue(ValueBase):
	Value: str

	pass

class Vector3Value(ValueBase):
	Value: Vector3

	pass

class Vector3Curve(Instance):
	@abstractmethod
	def GetValueAtTime(self, time: float) -> list[Any]:
		pass

	@abstractmethod
	def X(self) -> FloatCurve:
		pass

	@abstractmethod
	def Y(self) -> FloatCurve:
		pass

	@abstractmethod
	def Z(self) -> FloatCurve:
		pass


	pass

class VersionControlService(Instance):
	ScriptCollabEnabled: bool

	pass

class VideoCaptureService(Instance):
	Active: bool
	CameraID: str
	@abstractmethod
	def GetCameraDevices(self) -> 'Map':
		pass


	pass

class VirtualInputManager(Instance):
	AdditionalLuaState: str
	@abstractmethod
	def Dump(self) -> None:
		pass

	@abstractmethod
	def HandleGamepadAxisInput(self, objectId: int, keyCode: KeyCode, x: float, y: float, z: float) -> None:
		pass

	@abstractmethod
	def HandleGamepadButtonInput(self, deviceId: int, keyCode: KeyCode, buttonState: int) -> None:
		pass

	@abstractmethod
	def HandleGamepadConnect(self, deviceId: int) -> None:
		pass

	@abstractmethod
	def HandleGamepadDisconnect(self, deviceId: int) -> None:
		pass

	@abstractmethod
	def SendAccelerometerEvent(self, x: float, y: float, z: float) -> None:
		pass

	@abstractmethod
	def SendGravityEvent(self, x: float, y: float, z: float) -> None:
		pass

	@abstractmethod
	def SendGyroscopeEvent(self, quatX: float, quatY: float, quatZ: float, quatW: float) -> None:
		pass

	@abstractmethod
	def SendKeyEvent(self, isPressed: bool, keyCode: KeyCode, isRepeatedKey: bool, layerCollector: Instance) -> None:
		pass

	@abstractmethod
	def SendMouseButtonEvent(self, x: int, y: int, mouseButton: int, isDown: bool, layerCollector: Instance, repeatCount: int) -> None:
		pass

	@abstractmethod
	def SendMouseMoveEvent(self, x: float, y: float, layerCollector: Instance) -> None:
		pass

	@abstractmethod
	def SendMouseWheelEvent(self, x: float, y: float, isForwardScroll: bool, layerCollector: Instance) -> None:
		pass

	@abstractmethod
	def SendTextInputCharacterEvent(self, str: str, layerCollector: Instance) -> None:
		pass

	@abstractmethod
	def SendTouchEvent(self, touchId: int, state: int, x: float, y: float) -> None:
		pass

	@abstractmethod
	def SetInputTypesToIgnore(self, inputTypesToIgnore: Any) -> None:
		pass

	@abstractmethod
	def StartPlaying(self, fileName: str) -> None:
		pass

	@abstractmethod
	def StartPlayingJSON(self, string: str) -> None:
		pass

	@abstractmethod
	def StartRecording(self) -> None:
		pass

	@abstractmethod
	def StopPlaying(self) -> None:
		pass

	@abstractmethod
	def StopRecording(self) -> None:
		pass

	@abstractmethod
	def sendRobloxEvent(self, namespace: str, detail: str, detailType: str) -> None:
		pass

	@abstractmethod
	def sendThemeChangeEvent(self, themeName: str) -> None:
		pass

	@abstractmethod
	def WaitForInputEventsProcessed(self) -> None:
		pass


	pass

class VirtualUser(Instance):
	@abstractmethod
	def Button1Down(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def Button1Up(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def Button2Down(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def Button2Up(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def CaptureController(self) -> None:
		pass

	@abstractmethod
	def ClickButton1(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def ClickButton2(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def MoveMouse(self, position: Vector2, camera: CFrame) -> None:
		pass

	@abstractmethod
	def SetKeyDown(self, key: str) -> None:
		pass

	@abstractmethod
	def SetKeyUp(self, key: str) -> None:
		pass

	@abstractmethod
	def StartRecording(self) -> None:
		pass

	@abstractmethod
	def StopRecording(self) -> str:
		pass

	@abstractmethod
	def TypeKey(self, key: str) -> None:
		pass


	pass

class VisibilityService(Instance):

	pass

class Visit(Instance):

	pass

class VoiceChannel(Instance):
	@abstractmethod
	def AddUserAsync(self, userId: int) -> 'VoiceSource':
		pass


	pass

class VoiceChatInternal(Instance):
	VoiceChatState: VoiceChatState
	@abstractmethod
	def GetAndClearCallFailureMessage(self) -> str:
		pass

	@abstractmethod
	def GetAudioProcessingSettings(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetChannelId(self) -> str:
		pass

	@abstractmethod
	def GetGroupId(self) -> str:
		pass

	@abstractmethod
	def GetMicDevices(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetParticipants(self) -> list[Any]:
		pass

	@abstractmethod
	def GetSpeakerDevices(self) -> tuple[Any]:
		pass

	@abstractmethod
	def GetVoiceChatApiVersion(self) -> int:
		pass

	@abstractmethod
	def GetVoiceChatAvailable(self) -> int:
		pass

	@abstractmethod
	def IsContextVoiceEnabled(self) -> bool:
		pass

	@abstractmethod
	def IsPublishPaused(self) -> bool:
		pass

	@abstractmethod
	def IsSubscribePaused(self, userId: int) -> bool:
		pass

	@abstractmethod
	def JoinByGroupId(self, groupId: str, isMicMuted: bool) -> bool:
		pass

	@abstractmethod
	def JoinByGroupIdToken(self, groupId: str, isMicMuted: bool) -> bool:
		pass

	@abstractmethod
	def Leave(self) -> None:
		pass

	@abstractmethod
	def PublishPause(self, paused: bool) -> bool:
		pass

	@abstractmethod
	def SetMicDevice(self, micDeviceName: str, micDeviceGuid: str) -> None:
		pass

	@abstractmethod
	def SetSpeakerDevice(self, speakerDeviceName: str, speakerDeviceGuid: str) -> None:
		pass

	@abstractmethod
	def SubscribeBlock(self, userId: int) -> bool:
		pass

	@abstractmethod
	def SubscribePause(self, userId: int, paused: bool) -> bool:
		pass

	@abstractmethod
	def SubscribePauseAll(self, paused: bool) -> bool:
		pass

	@abstractmethod
	def SubscribeRetry(self, userId: int) -> bool:
		pass

	@abstractmethod
	def SubscribeUnblock(self, userId: int) -> bool:
		pass

	@abstractmethod
	def IsVoiceEnabledForUserIdAsync(self, userId: int) -> bool:
		pass


	pass

class VoiceChatService(Instance):
	EnableDefaultVoice: bool
	VoiceChatEnabledForPlaceOnRcc: bool
	VoiceChatEnabledForUniverseOnRcc: bool
	@abstractmethod
	def IsVoiceEnabledForUserIdAsync(self, userId: int) -> bool:
		pass


	pass

class VoiceSource(Instance):
	UserId: int

	pass

class WeldConstraint(Instance):
	Active: bool
	Enabled: bool
	Part0: BasePart
	Part1: BasePart

	pass

