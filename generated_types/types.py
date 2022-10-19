from typing_extensions import Self
from typing import Any, Callable, Tuple
from enum import Enum

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
	Parent: Self
	RobloxLocked: bool
	SourceAssetId: int
	archivable: bool
	className: str
	def ClearAllChildren(self):
		pass

	def Clone(self):
		pass

	def Destroy(self):
		pass

	def FindFirstAncestor(self, name: str):
		pass

	def FindFirstAncestorOfClass(self, className: str):
		pass

	def FindFirstAncestorWhichIsA(self, className: str):
		pass

	def FindFirstChild(self, name: str, recursive: bool):
		pass

	def FindFirstChildOfClass(self, className: str):
		pass

	def FindFirstChildWhichIsA(self, className: str, recursive: bool):
		pass

	def FindFirstDescendant(self, name: str):
		pass

	def GetActor(self):
		pass

	def GetAttribute(self, attribute: str):
		pass

	def GetAttributeChangedSignal(self, attribute: str):
		pass

	def GetAttributes(self):
		pass

	def GetChildren(self):
		pass

	def GetDebugId(self, scopeLength: int):
		pass

	def GetDescendants(self):
		pass

	def GetFullName(self):
		pass

	def GetPropertyChangedSignal(self, property: str):
		pass

	def IsA(self, className: str):
		pass

	def IsAncestorOf(self, descendant: Self):
		pass

	def IsDescendantOf(self, ancestor: Self):
		pass

	def Remove(self):
		pass

	def SetAttribute(self, attribute: str, value: Any):
		pass

	def WaitForChild(self, childName: str, timeOut: float):
		pass

	def children(self):
		pass

	def clone(self):
		pass

	def destroy(self):
		pass

	def findFirstChild(self, name: str, recursive: bool):
		pass

	def getChildren(self):
		pass

	def isA(self, className: str):
		pass

	def isDescendantOf(self, ancestor: Self):
		pass

	def remove(self):
		pass


	pass

class Accoutrement:
	AttachmentForward: Vector3
	AttachmentPoint: CFrame
	AttachmentPos: Vector3
	AttachmentRight: Vector3
	AttachmentUp: Vector3

	pass

class Accessory:
	AccessoryType: AccessoryType

	pass

class Hat:

	pass

class AdPortal:
	PortalInvalidReason: str
	PortalStatus: AdPortalStatus
	PortalType: AdPortalType
	PortalVersion: int

	pass

class AdService:
	def ShowVideoAd(self):
		pass


	pass

class AdvancedDragger:

	pass

class AnalyticsService:
	ApiKey: str
	def FireCustomEvent(self, player: Instance, eventCategory: str, customData: Any):
		pass

	def FireEvent(self, category: str, value: Any):
		pass

	def FireInGameEconomyEvent(self, player: Instance, itemName: str, economyAction: AnalyticsEconomyAction, itemCategory: str, amount: int, currency: str, location: Any, customData: Any):
		pass

	def FireLogEvent(self, player: Instance, logLevel: AnalyticsLogLevel, message: str, debugInfo: Any, customData: Any):
		pass

	def FirePlayerProgressionEvent(self, player: Instance, category: str, progressionStatus: AnalyticsProgressionStatus, location: Any, statistics: Any, customData: Any):
		pass


	pass

class Animation:
	AnimationId: Content

	pass

class AnimationClip:
	Loop: bool
	Priority: AnimationPriority

	pass

class CurveAnimation:

	pass

class KeyframeSequence:
	AuthoredHipHeight: float
	def AddKeyframe(self, keyframe: Instance):
		pass

	def GetKeyframes(self):
		pass

	def RemoveKeyframe(self, keyframe: Instance):
		pass


	pass

class AnimationClipProvider:
	def GetAnimationClip(self, assetId: Content):
		pass

	def GetAnimationClipById(self, assetId: int, useCache: bool):
		pass

	def GetMemStats(self):
		pass

	def RegisterActiveAnimationClip(self, animationClip: AnimationClip):
		pass

	def RegisterAnimationClip(self, animationClip: AnimationClip):
		pass

	def GetAnimationClipAsync(self, assetId: Content):
		pass

	def GetAnimations(self, userId: int):
		pass


	pass

class AnimationController:
	def GetPlayingAnimationTracks(self):
		pass

	def LoadAnimation(self, animation: Animation):
		pass


	pass

class AnimationFromVideoCreatorService:
	def CreateJob(self, filePath: str):
		pass

	def DownloadJobResult(self, jobId: str, outputFilePath: str):
		pass

	def FullProcess(self, videoFilePath: str, progressCallback: Callable[..., Any]):
		pass

	def GetJobStatus(self, jobId: str):
		pass


	pass

class AnimationFromVideoCreatorStudioService:
	def IsAgeRestricted(self):
		pass

	def CreateAnimationByUploadingVideo(self, progressCallback: Callable[..., Any]):
		pass

	def ImportVideoWithPrompt(self):
		pass


	pass

class AnimationRigData:
	def LoadFromHumanoid(self, humanoid: Instance):
		pass


	pass

class AnimationStreamTrack:
	Animation: TrackerStreamAnimation
	IsPlaying: bool
	Priority: AnimationPriority
	WeightCurrent: float
	WeightTarget: float
	def AdjustWeight(self, weight: float, fadeTime: float):
		pass

	def GetTrackerData(self):
		pass

	def Play(self, fadeTime: float, weight: float):
		pass

	def Stop(self, fadeTime: float):
		pass


	pass

class AnimationTrack:
	IsPlaying: bool
	Length: float
	Looped: bool
	Priority: AnimationPriority
	Speed: float
	TimePosition: float
	WeightCurrent: float
	WeightTarget: float
	Animation: Animation
	def AdjustSpeed(self, speed: float):
		pass

	def AdjustWeight(self, weight: float, fadeTime: float):
		pass

	def GetMarkerReachedSignal(self, name: str):
		pass

	def GetTimeOfKeyframe(self, keyframeName: str):
		pass

	def Play(self, fadeTime: float, weight: float, speed: float):
		pass

	def Stop(self, fadeTime: float):
		pass


	pass

class Animator:
	PreferLodEnabled: bool
	def ApplyJointVelocities(self, motors: Any):
		pass

	def GetPlayingAnimationTracks(self):
		pass

	def GetPlayingAnimationTracksCoreScript(self):
		pass

	def LoadAnimation(self, animation: Animation):
		pass

	def LoadAnimationCoreScript(self, animation: Animation):
		pass

	def LoadStreamAnimation(self, animation: TrackerStreamAnimation):
		pass

	def StepAnimations(self, deltaTime: float):
		pass


	pass

class AppUpdateService:
	def CheckForUpdate(self, handler: Callable[..., Any]):
		pass

	def DisableDUAR(self):
		pass

	def DisableDUARAndOpenSurvey(self, surveyUrl: str):
		pass

	def PerformManagedUpdate(self):
		pass


	pass

class AssetCounterService:

	pass

class AssetDeliveryProxy:
	Interface: str
	Port: int
	StartServer: bool

	pass

class AssetImportService:
	def PickFileWithPrompt(self):
		pass

	def StartSessionWithPrompt(self):
		pass


	pass

class AssetImportSession:
	def Cancel(self):
		pass

	def GetCurrentStatusTable(self):
		pass

	def GetFilename(self):
		pass

	def GetInstance(self, nodeId: int):
		pass

	def GetSettingsRoot(self):
		pass

	def IsAvatar(self):
		pass

	def Upload(self):
		pass


	pass

class AssetManagerService:
	def GetMeshIdFromAliasName(self, aliasName: str):
		pass

	def GetMeshIdFromAssetId(self, assetId: int):
		pass

	def GetTextureIdFromAliasName(self, aliasName: str):
		pass

	def GetTextureIdFromAssetId(self, assetId: int):
		pass

	def HasUnpublishedChangesForLinkedSource(self, aliasName: str):
		pass

	def InsertAudio(self, assetId: int, assetName: str):
		pass

	def InsertImage(self, assetId: int):
		pass

	def InsertLinkedSourceAsLocalScript(self, aliasName: str):
		pass

	def InsertLinkedSourceAsModuleScript(self, aliasName: str):
		pass

	def InsertLinkedSourceAsScript(self, aliasName: str):
		pass

	def InsertMesh(self, aliasName: str, insertWithLocation: bool):
		pass

	def InsertMeshesWithLocation(self, aliasNames: list[Any]):
		pass

	def InsertModel(self, modelId: int):
		pass

	def InsertPackage(self, packageId: int):
		pass

	def InsertVideo(self, assetId: int, assetName: str):
		pass

	def OpenLinkedSource(self, aliasName: str):
		pass

	def OpenPlace(self, placeId: int):
		pass

	def RefreshLinkedSource(self, aliasName: str):
		pass

	def RevertLinkedSourceToLastPublishedVersion(self, aliasName: str):
		pass

	def ShowPackageDetails(self, packageId: int):
		pass

	def UpdateAllPackages(self, packageId: int):
		pass

	def ViewPackageOnWebsite(self, packageId: int):
		pass

	def AddNewPlace(self):
		pass

	def CreateAlias(self, assetType: int, assetId: int, aliasName: str):
		pass

	def DeleteAlias(self, aliasName: str):
		pass

	def PublishLinkedSource(self, assetId: int, aliasName: str):
		pass

	def RemovePlace(self, placeId: int):
		pass

	def RenameAlias(self, assetType: int, assetId: int, oldAliasName: str, newAliasName: str):
		pass

	def RenameModel(self, modelId: int, newName: str):
		pass

	def RenamePlace(self, placeId: int, newName: str):
		pass


	pass

class AssetPatchSettings:
	ContentId: str
	OutputPath: str
	PatchId: str

	pass

class AssetService:
	def GetBundleDetailsSync(self, bundleId: int):
		pass

	def CreatePlaceAsync(self, placeName: str, templatePlaceID: int, description: str):
		pass

	def CreatePlaceInPlayerInventoryAsync(self, player: Instance, placeName: str, templatePlaceID: int, description: str):
		pass

	def GetAssetIdsForPackage(self, packageAssetId: int):
		pass

	def GetAssetThumbnailAsync(self, assetId: int, thumbnailSize: Vector2, assetType: int):
		pass

	def GetBundleDetailsAsync(self, bundleId: int):
		pass

	def GetCreatorAssetID(self, creationID: int):
		pass

	def GetGamePlacesAsync(self):
		pass

	def SavePlaceAsync(self):
		pass


	pass

class Atmosphere:
	Color: Color3
	Decay: Color3
	Density: float
	Glare: float
	Haze: float
	Offset: float

	pass

class Attachment:
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
	def GetAxis(self):
		pass

	def GetSecondaryAxis(self):
		pass

	def SetAxis(self, axis: Vector3):
		pass

	def SetSecondaryAxis(self, axis: Vector3):
		pass


	pass

class Bone:
	IsCFrameDriven: bool
	Transform: CFrame
	TransformedCFrame: CFrame
	TransformedWorldCFrame: CFrame

	pass

class AvatarEditorService:
	def GetAccessoryType(self, avatarAssetType: AvatarAssetType):
		pass

	def NoPromptCreateOutfit(self, humanoidDescription: HumanoidDescription, rigType: HumanoidRigType, name: str):
		pass

	def NoPromptDeleteOutfit(self, outfitId: int):
		pass

	def NoPromptRenameOutfit(self, outfitId: int, name: str):
		pass

	def NoPromptSaveAvatar(self, humanoidDescription: HumanoidDescription, rigType: HumanoidRigType, saveDict: Dictionary, gearAssetId: int):
		pass

	def NoPromptSetFavorite(self, itemId: int, itemType: AvatarItemType, shouldFavorite: bool):
		pass

	def NoPromptUpdateOutfit(self, outfitId: int, humanoidDescription: HumanoidDescription, rigType: HumanoidRigType):
		pass

	def PerformCreateOutfitWithDescription(self, humanoidDescription: HumanoidDescription, name: str):
		pass

	def PerformDeleteOutfit(self):
		pass

	def PerformRenameOutfit(self, name: str):
		pass

	def PerformSaveAvatarWithDescription(self, humanoidDescription: HumanoidDescription, addedAssets: list[Any], removedAssets: list[Any]):
		pass

	def PerformSetFavorite(self):
		pass

	def PerformUpdateOutfit(self, humanoidDescription: HumanoidDescription):
		pass

	def PromptAllowInventoryReadAccess(self):
		pass

	def PromptCreateOutfit(self, outfit: HumanoidDescription, rigType: HumanoidRigType):
		pass

	def PromptDeleteOutfit(self, outfitId: int):
		pass

	def PromptRenameOutfit(self, outfitId: int):
		pass

	def PromptSaveAvatar(self, humanoidDescription: HumanoidDescription, rigType: HumanoidRigType):
		pass

	def PromptSetFavorite(self, itemId: int, itemType: AvatarItemType, shouldFavorite: bool):
		pass

	def PromptUpdateOutfit(self, outfitId: int, updatedOutfit: HumanoidDescription, rigType: HumanoidRigType):
		pass

	def SetAllowInventoryReadAccess(self, inventoryReadAccessGranted: bool):
		pass

	def SignalCreateOutfitFailed(self):
		pass

	def SignalCreateOutfitPermissionDenied(self):
		pass

	def SignalDeleteOutfitFailed(self):
		pass

	def SignalDeleteOutfitPermissionDenied(self):
		pass

	def SignalRenameOutfitFailed(self):
		pass

	def SignalRenameOutfitPermissionDenied(self):
		pass

	def SignalSaveAvatarFailed(self):
		pass

	def SignalSaveAvatarPermissionDenied(self):
		pass

	def SignalSetFavoriteFailed(self):
		pass

	def SignalSetFavoritePermissionDenied(self):
		pass

	def SignalUpdateOutfitFailed(self):
		pass

	def SignalUpdateOutfitPermissionDenied(self):
		pass

	def CheckApplyDefaultClothing(self, humanoidDescription: HumanoidDescription):
		pass

	def ConformToAvatarRules(self, humanoidDescription: HumanoidDescription):
		pass

	def GetAvatarRules(self):
		pass

	def GetBatchItemDetails(self, itemIds: list[Any], itemType: AvatarItemType):
		pass

	def GetFavorite(self, itemId: int, itemType: AvatarItemType):
		pass

	def GetInventory(self, assetTypes: list[Any]):
		pass

	def GetItemDetails(self, itemId: int, itemType: AvatarItemType):
		pass

	def GetOutfits(self, outfitSource: OutfitSource, outfitType: OutfitType):
		pass

	def GetRecommendedAssets(self, assetType: AvatarAssetType, contextAssetId: int):
		pass

	def GetRecommendedAssetsV2(self, assetType: AvatarAssetType, assetId: int, numItems: int, includeDetails: bool):
		pass

	def GetRecommendedBundles(self, bundleId: int):
		pass

	def GetRecommendedBundlesV2(self, bundleType: BundleType, bundleId: int, numItems: int, includeDetails: bool):
		pass

	def SearchCatalog(self, searchParameters: CatalogSearchParams):
		pass


	pass

class AvatarImportService:
	def ImportFBXAnimationFromFilePathUserMayChooseModel(self, fbxFilePath: str, selectedRig: Instance, userChooseModelThenImportCB: Callable[..., Any]):
		pass

	def ImportFBXAnimationUserMayChooseModel(self, selectedRig: Instance, userChooseModelThenImportCB: Callable[..., Any]):
		pass

	def ImportFbxRigWithoutSceneLoad(self, isR15: bool):
		pass

	def ImportLoadedFBXAnimation(self, useFBXModel: bool):
		pass

	def LoadRigAndDetectType(self, promptR15Callback: Callable[..., Any]):
		pass


	pass

class Backpack:

	pass

class BackpackItem:
	TextureId: Content

	pass

class HopperBin:
	Active: bool
	BinType: BinType
	def Disable(self):
		pass

	def ToggleSelect(self):
		pass


	pass

class Tool:
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
	def Activate(self):
		pass

	def Deactivate(self):
		pass


	pass

class Flag:
	TeamColor: BrickColor

	pass

class BadgeService:
	def AwardBadge(self, userId: int, badgeId: int):
		pass

	def GetBadgeInfoAsync(self, badgeId: int):
		pass

	def IsDisabled(self, badgeId: int):
		pass

	def IsLegal(self, badgeId: int):
		pass

	def UserHasBadge(self, userId: int, badgeId: int):
		pass

	def UserHasBadgeAsync(self, userId: int, badgeId: int):
		pass


	pass

class BasePlayerGui:
	def GetGuiObjectsAtPosition(self, x: int, y: int):
		pass

	def GetGuiObjectsInCircle(self, position: Vector2, radius: float):
		pass


	pass

class CoreGui:
	SelectionImageObject: GuiObject
	Version: int
	def SetUserGuiRendering(self, enabled: bool, guiAdornee: Instance, faceId: NormalId):
		pass

	def TakeScreenshot(self):
		pass

	def ToggleRecording(self):
		pass


	pass

class PlayerGui:
	CurrentScreenOrientation: ScreenOrientation
	SelectionImageObject: GuiObject
	ScreenOrientation: ScreenOrientation
	def GetTopbarTransparency(self):
		pass

	def SetTopbarTransparency(self, transparency: float):
		pass


	pass

class StarterGui:
	ProcessUserInput: bool
	ResetPlayerGuiOnSpawn: bool
	ShowDevelopmentGui: bool
	ScreenOrientation: ScreenOrientation
	VirtualCursorMode: VirtualCursorMode
	def GetCoreGuiEnabled(self, coreGuiType: CoreGuiType):
		pass

	def RegisterGetCore(self, parameterName: str, getFunction: Callable[..., Any]):
		pass

	def RegisterSetCore(self, parameterName: str, setFunction: Callable[..., Any]):
		pass

	def SetCore(self, parameterName: str, value: Any):
		pass

	def SetCoreGuiEnabled(self, coreGuiType: CoreGuiType, enabled: bool):
		pass

	def GetCore(self, parameterName: str):
		pass


	pass

class BaseWrap:
	CageMeshId: Content
	CageOrigin: CFrame
	CageOriginWorld: CFrame
	HSRAssetId: Content
	ImportOrigin: CFrame
	ImportOriginWorld: CFrame
	def GetFaces(self, cageType: CageType):
		pass

	def GetVertices(self, cageType: CageType):
		pass

	def IsHSRReady(self):
		pass

	def ModifyVertices(self, cageType: CageType, vertices: list[Any]):
		pass


	pass

class WrapLayer:
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

class WrapTarget:
	Color: Color3
	DebugMode: WrapTargetDebugMode
	Stiffness: float

	pass

class Beam:
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
	def SetTextureOffset(self, offset: float):
		pass


	pass

class BindableEvent:
	def Fire(self, arguments: tuple[Any]):
		pass


	pass

class BindableFunction:
	def Invoke(self, arguments: tuple[Any]):
		pass


	pass

class BodyMover:

	pass

class BodyAngularVelocity:
	AngularVelocity: Vector3
	MaxTorque: Vector3
	P: float
	angularvelocity: Vector3
	maxTorque: Vector3

	pass

class BodyForce:
	Force: Vector3
	force: Vector3

	pass

class BodyGyro:
	D: float
	MaxTorque: Vector3
	P: float
	cframe: CFrame
	maxTorque: Vector3
	CFrame: CFrame

	pass

class BodyPosition:
	D: float
	MaxForce: Vector3
	P: float
	Position: Vector3
	maxForce: Vector3
	position: Vector3
	def GetLastForce(self):
		pass

	def lastForce(self):
		pass


	pass

class BodyThrust:
	Force: Vector3
	Location: Vector3
	force: Vector3
	location: Vector3

	pass

class BodyVelocity:
	MaxForce: Vector3
	P: float
	Velocity: Vector3
	maxForce: Vector3
	velocity: Vector3
	def GetLastForce(self):
		pass

	def lastForce(self):
		pass


	pass

class RocketPropulsion:
	CartoonFactor: float
	MaxSpeed: float
	MaxThrust: float
	MaxTorque: Vector3
	Target: BasePart
	TargetOffset: Vector3
	TargetRadius: float
	ThrustD: float
	ThrustP: float
	TurnD: float
	TurnP: float
	def Abort(self):
		pass

	def Fire(self):
		pass

	def fire(self):
		pass


	pass

class Breakpoint:
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

class BrowserService:
	def CloseBrowserWindow(self):
		pass

	def CopyAuthCookieFromBrowserToEngine(self):
		pass

	def EmitHybridEvent(self, moduleName: str, eventName: str, params: str):
		pass

	def ExecuteJavaScript(self, javascript: str):
		pass

	def OpenBrowserWindow(self, url: str):
		pass

	def OpenNativeOverlay(self, title: str, url: str):
		pass

	def OpenWeChatAuthWindow(self):
		pass

	def ReturnToJavaScript(self, callbackId: str, success: bool, params: str):
		pass

	def SendCommand(self, command: str):
		pass


	pass

class BulkImportService:
	def LaunchBulkImport(self, assetTypeToImport: int):
		pass

	def ShowBulkImportView(self):
		pass


	pass

class CacheableContentProvider:

	pass

class HSRDataContentProvider:

	pass

class MeshContentProvider:
	def GetContentMemoryData(self):
		pass


	pass

class SolidModelContentProvider:

	pass

class CalloutService:
	def AttachCallout(self, definitionId: str, locationId: str, target: Instance):
		pass

	def DefineCallout(self, definitionId: str, title: str, description: str, learnMoreURL: str):
		pass

	def DetachCalloutsByDefinitionId(self, definitionId: str):
		pass


	pass

class Camera:
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
	def GetLargestCutoffDistance(self, ignoreList: Objects):
		pass

	def GetPanSpeed(self):
		pass

	def GetPartsObscuringTarget(self, castPoints: list[Any], ignoreList: Objects):
		pass

	def GetRenderCFrame(self):
		pass

	def GetRoll(self):
		pass

	def GetTiltSpeed(self):
		pass

	def Interpolate(self, endPos: CFrame, endFocus: CFrame, duration: float):
		pass

	def PanUnits(self, units: int):
		pass

	def ScreenPointToRay(self, x: float, y: float, depth: float):
		pass

	def SetCameraPanMode(self, mode: CameraPanMode):
		pass

	def SetImageServerView(self, modelCoord: CFrame):
		pass

	def SetRoll(self, rollAngle: float):
		pass

	def TiltUnits(self, units: int):
		pass

	def ViewportPointToRay(self, x: float, y: float, depth: float):
		pass

	def WorldToScreenPoint(self, worldPoint: Vector3):
		pass

	def WorldToViewportPoint(self, worldPoint: Vector3):
		pass

	def Zoom(self, distance: float):
		pass


	pass

class ChangeHistoryService:
	def GetCanRedo(self):
		pass

	def GetCanUndo(self):
		pass

	def Redo(self):
		pass

	def ResetWaypoints(self):
		pass

	def SetEnabled(self, state: bool):
		pass

	def SetWaypoint(self, name: str):
		pass

	def Undo(self):
		pass


	pass

class CharacterAppearance:

	pass

class BodyColors:
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

class CharacterMesh:
	BaseTextureId: int
	MeshId: int
	OverlayTextureId: int
	BodyPart: BodyPart

	pass

class Clothing:
	Color3: Color3

	pass

class Pants:
	PantsTemplate: Content

	pass

class Shirt:
	ShirtTemplate: Content

	pass

class ShirtGraphic:
	Graphic: Content
	Color3: Color3

	pass

class Skin:
	SkinColor: BrickColor

	pass

class Chat:
	BubbleChatEnabled: bool
	LoadDefaultChat: bool
	def Chat(self, partOrCharacter: Instance, message: str, color: ChatColor):
		pass

	def ChatLocal(self, partOrCharacter: Instance, message: str, color: ChatColor):
		pass

	def GetShouldUseLuaChat(self):
		pass

	def InvokeChatCallback(self, callbackType: ChatCallbackType, callbackArguments: tuple[Any]):
		pass

	def RegisterChatCallback(self, callbackType: ChatCallbackType, callbackFunction: Callable[..., Any]):
		pass

	def SetBubbleChatSettings(self, settings: Any):
		pass

	def CanUserChatAsync(self, userId: int):
		pass

	def CanUsersChatAsync(self, userIdFrom: int, userIdTo: int):
		pass

	def FilterStringAsync(self, stringToFilter: str, playerFrom: Player, playerTo: Player):
		pass

	def FilterStringForBroadcast(self, stringToFilter: str, playerFrom: Player):
		pass

	def FilterStringForPlayerAsync(self, stringToFilter: str, playerToFilterFor: Player):
		pass


	pass

class ClickDetector:
	CursorIcon: Content
	MaxActivationDistance: float

	pass

class Clouds:
	Color: Color3
	Cover: float
	Density: float
	Enabled: bool

	pass

class ClusterPacketCache:

	pass

class CollectionService:
	def AddTag(self, instance: Instance, tag: str):
		pass

	def GetAllTags(self):
		pass

	def GetCollection(self, class: str):
		pass

	def GetInstanceAddedSignal(self, tag: str):
		pass

	def GetInstanceRemovedSignal(self, tag: str):
		pass

	def GetTagged(self, tag: str):
		pass

	def GetTags(self, instance: Instance):
		pass

	def HasTag(self, instance: Instance, tag: str):
		pass

	def RemoveTag(self, instance: Instance, tag: str):
		pass


	pass

class CommandInstance:
	AllowGUIAccessPoints: bool
	Checked: bool
	DefaultShortcut: str
	DisplayName: str
	Enabled: bool
	Icon: str
	Name: str
	Permission: CommandPermission
	StatusTip: str
	def EnableGuiAccess(self, displayName: str, statusTip: str, defaultShortcut: str):
		pass

	def RegisterExecutionCallback(self, callbackFunction: Callable[..., Any]):
		pass


	pass

class CommandService:
	def Execute(self, name: str, params: Any):
		pass

	def RegisterCommand(self, plugin: Plugin, name: str, context: str, permission: CommandPermission):
		pass


	pass

class Configuration:

	pass

class ConfigureServerService:

	pass

class Constraint:
	Active: bool
	Attachment0: Attachment
	Attachment1: Attachment
	Color: BrickColor
	Enabled: bool
	Visible: bool

	pass

class AlignOrientation:
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

class AlignPosition:
	ApplyAtCenterOfMass: bool
	MaxForce: float
	MaxVelocity: float
	Mode: PositionAlignmentMode
	Position: Vector3
	ReactionForceEnabled: bool
	Responsiveness: float
	RigidityEnabled: bool

	pass

class AngularVelocity:
	AngularVelocity: Vector3
	MaxTorque: float
	ReactionTorqueEnabled: bool
	RelativeTo: ActuatorRelativeTo

	pass

class AnimationConstraint:
	MaxForce: float
	MaxTorque: float
	Transform: CFrame

	pass

class BallSocketConstraint:
	LimitsEnabled: bool
	MaxFrictionTorque: float
	Radius: float
	Restitution: float
	TwistLimitsEnabled: bool
	TwistLowerAngle: float
	TwistUpperAngle: float
	UpperAngle: float

	pass

class HingeConstraint:
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

class LineForce:
	ApplyAtCenterOfMass: bool
	InverseSquareLaw: bool
	Magnitude: float
	MaxForce: float
	ReactionForceEnabled: bool

	pass

class LinearVelocity:
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

class PlaneConstraint:

	pass

class Plane:

	pass

class RigidConstraint:

	pass

class RodConstraint:
	CurrentDistance: float
	Length: float
	LimitAngle0: float
	LimitAngle1: float
	LimitsEnabled: bool
	Thickness: float

	pass

class RopeConstraint:
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

class SlidingBallConstraint:
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

class CylindricalConstraint:
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

class PrismaticConstraint:

	pass

class SpringConstraint:
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

class Torque:
	RelativeTo: ActuatorRelativeTo
	Torque: Vector3

	pass

class TorsionSpringConstraint:
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

class UniversalConstraint:
	LimitsEnabled: bool
	MaxAngle: float
	Radius: float
	Restitution: float

	pass

class VectorForce:
	ApplyAtCenterOfMass: bool
	Force: Vector3
	RelativeTo: ActuatorRelativeTo

	pass

class ContentProvider:
	BaseUrl: str
	RequestQueueSize: int
	def CalculateNumTrianglesInMeshSync(self, meshId: str):
		pass

	def GetDetailedFailedRequests(self):
		pass

	def GetFailedRequests(self):
		pass

	def ListEncryptedAssets(self):
		pass

	def Preload(self, contentId: Content):
		pass

	def RegisterDefaultEncryptionKey(self, encryptionKey: str):
		pass

	def RegisterDefaultSessionKey(self, sessionKey: str):
		pass

	def RegisterEncryptedAsset(self, assetId: Content, encryptionKey: str):
		pass

	def RegisterSessionEncryptedAsset(self, contentId: Content, sessionKey: str):
		pass

	def SetBaseUrl(self, url: str):
		pass

	def UnregisterDefaultEncryptionKey(self):
		pass

	def UnregisterEncryptedAsset(self, assetId: Content):
		pass

	def CalculateNumTrianglesInMesh(self, meshId: str):
		pass

	def PreloadAsync(self, contentIdList: list[Any], callbackFunction: Callable[..., Any]):
		pass


	pass

class ContextActionService:
	def BindAction(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]):
		pass

	def BindActionAtPriority(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, priorityLevel: int, inputTypes: tuple[Any]):
		pass

	def BindActionToInputTypes(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]):
		pass

	def BindActivate(self, userInputTypeForActivation: UserInputType, keyCodesForActivation: tuple[Any]):
		pass

	def BindCoreAction(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, inputTypes: tuple[Any]):
		pass

	def BindCoreActionAtPriority(self, actionName: str, functionToBind: Callable[..., Any], createTouchButton: bool, priorityLevel: int, inputTypes: tuple[Any]):
		pass

	def CallFunction(self, actionName: str, state: UserInputState, inputObject: Instance):
		pass

	def FireActionButtonFoundSignal(self, actionName: str, actionButton: Instance):
		pass

	def GetAllBoundActionInfo(self):
		pass

	def GetAllBoundCoreActionInfo(self):
		pass

	def GetBoundActionInfo(self, actionName: str):
		pass

	def GetBoundCoreActionInfo(self, actionName: str):
		pass

	def GetCurrentLocalToolIcon(self):
		pass

	def SetDescription(self, actionName: str, description: str):
		pass

	def SetImage(self, actionName: str, image: str):
		pass

	def SetPosition(self, actionName: str, position: UDim2):
		pass

	def SetTitle(self, actionName: str, title: str):
		pass

	def UnbindAction(self, actionName: str):
		pass

	def UnbindActivate(self, userInputTypeForActivation: UserInputType, keyCodeForActivation: KeyCode):
		pass

	def UnbindAllActions(self):
		pass

	def UnbindCoreAction(self, actionName: str):
		pass

	def GetButton(self, actionName: str):
		pass


	pass

class Controller:
	def BindButton(self, button: Button, caption: str):
		pass

	def GetButton(self, button: Button):
		pass

	def UnbindButton(self, button: Button):
		pass

	def bindButton(self, button: Button, caption: str):
		pass

	def getButton(self, button: Button):
		pass


	pass

class HumanoidController:

	pass

class SkateboardController:
	Steer: float
	Throttle: float

	pass

class VehicleController:

	pass

class ControllerBase:
	MoveSpeedFactor: float
	RigidityEnabled: bool

	pass

class AirController:
	CancelAirMomentum: bool
	MoveMaxForce: float
	OrientationMaxTorque: float
	OrientationSpeedFactor: float
	VectorForce: Vector3

	pass

class ClimbController:
	AccelerationTime: float
	MoveMaxForce: float
	OrientationMaxTorque: float
	OrientationSpeedFactor: float

	pass

class GroundController:
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

class SwimController:
	AccelerationTime: float
	PitchMaxTorque: float
	PitchSpeedFactor: float
	RollMaxTorque: float
	RollSpeedFactor: float

	pass

class ControllerManager:
	ActiveController: ControllerBase
	BaseMoveSpeed: float
	BaseTurnSpeed: float
	FacingDirection: Vector3
	HipHeight: float
	MovingDirection: Vector3
	def GetControllers(self):
		pass


	pass

class ControllerService:

	pass

class CookiesService:

	pass

class CorePackages:

	pass

class CoreScriptSyncService:
	def GetScriptFilePath(self, script: Instance):
		pass


	pass

class CrossDMScriptChangeListener:
	def IsWatchingScriptLine(self, scriptRef: str, lineNumber: int):
		pass

	def StartWatchingScriptLine(self, scriptRef: str, debuggerConnectionId: int, lineNumber: int):
		pass


	pass

class CustomEvent:
	def GetAttachedReceivers(self):
		pass

	def SetValue(self, newValue: float):
		pass


	pass

class CustomEventReceiver:
	Source: Instance
	def GetCurrentValue(self):
		pass


	pass

class DataModelMesh:
	Offset: Vector3
	Scale: Vector3
	VertexColor: Vector3

	pass

class BevelMesh:

	pass

class BlockMesh:

	pass

class CylinderMesh:

	pass

class FileMesh:
	MeshId: Content
	TextureId: Content

	pass

class SpecialMesh:
	MeshType: MeshType

	pass

class DataModelPatchService:
	def GetPatch(self, patchName: str):
		pass

	def RegisterPatch(self, patchName: str, behaviorName: str, localConfigPath: str, userId: int):
		pass

	def UpdatePatch(self, userId: int, patchName: str, callbackFunction: Callable[..., Any]):
		pass


	pass

class DataModelSession:
	CurrentDataModelType: StudioDataModelType
	SessionId: str

	pass

class DataStoreIncrementOptions:
	def GetMetadata(self):
		pass

	def SetMetadata(self, attributes: Dictionary):
		pass


	pass

class DataStoreInfo:
	CreatedTime: int
	DataStoreName: str
	UpdatedTime: int

	pass

class DataStoreKey:
	KeyName: str

	pass

class DataStoreKeyInfo:
	CreatedTime: int
	UpdatedTime: int
	Version: str
	def GetMetadata(self):
		pass

	def GetUserIds(self):
		pass


	pass

class DataStoreObjectVersionInfo:
	CreatedTime: int
	IsDeleted: bool
	Version: str

	pass

class DataStoreOptions:
	AllScopes: bool
	def SetExperimentalFeatures(self, experimentalFeatures: Dictionary):
		pass


	pass

class DataStoreService:
	AutomaticRetry: bool
	LegacyNamingScheme: bool
	def GetDataStore(self, name: str, scope: str, options: Instance):
		pass

	def GetGlobalDataStore(self):
		pass

	def GetOrderedDataStore(self, name: str, scope: str):
		pass

	def GetRequestBudgetForRequestType(self, requestType: DataStoreRequestType):
		pass

	def ListDataStoresAsync(self, prefix: str, pageSize: int, cursor: str):
		pass


	pass

class DataStoreSetOptions:
	def GetMetadata(self):
		pass

	def SetMetadata(self, attributes: Dictionary):
		pass


	pass

class Debris:
	MaxItems: int
	def AddItem(self, item: Instance, lifetime: float):
		pass

	def SetLegacyMaxItems(self, enabled: bool):
		pass

	def addItem(self, item: Instance, lifetime: float):
		pass


	pass

class DebugSettings:
	DataModel: int
	InstanceCount: int
	IsScriptStackTracingEnabled: bool
	JobCount: int
	PlayerCount: int
	ReportSoundWarnings: bool
	RobloxVersion: str
	TickCountPreciseOverride: TickCountSampleMethod

	pass

class DebuggablePluginWatcher:

	pass

class DebuggerBreakpoint:
	Condition: str
	ContinueExecution: bool
	IsEnabled: bool
	Line: int
	LogExpression: str
	isContextDependentBreakpoint: bool

	pass

class DebuggerConnection:
	ErrorMessage: str
	HasError: bool
	Id: int
	IsPaused: bool
	def AddBreakpoint(self, script: str, line: int, breakpoint: Breakpoint):
		pass

	def Close(self):
		pass

	def EvaluateWatch(self, expression: str, frame: StackFrame, callback: Callable[..., Any]):
		pass

	def GetFrameById(self, id: int):
		pass

	def GetSource(self, scriptRef: str, status: Callable[..., Any]):
		pass

	def GetThreadById(self, id: int):
		pass

	def GetThreads(self, callback: Callable[..., Any]):
		pass

	def GetVariableById(self, id: int):
		pass

	def Pause(self, thread: ThreadState, status: Callable[..., Any]):
		pass

	def Populate(self, instance: Instance, callback: Callable[..., Any]):
		pass

	def RemoveBreakpoint(self, breakpoint: Breakpoint):
		pass

	def Resume(self, thread: ThreadState, status: Callable[..., Any]):
		pass

	def SetExceptionBreakMode(self, breakMode: DebuggerExceptionBreakMode, callback: Callable[..., Any]):
		pass

	def SetVariable(self, variable: DebuggerVariable, value: str, callback: Callable[..., Any]):
		pass

	def Step(self, thread: ThreadState, callback: Callable[..., Any]):
		pass

	def StepIn(self, thread: ThreadState, callback: Callable[..., Any]):
		pass

	def StepOut(self, thread: ThreadState, callback: Callable[..., Any]):
		pass

	def UpdateSelectedFrame(self, threadId: int, frameNumber: int):
		pass


	pass

class LocalDebuggerConnection:

	pass

class DebuggerConnectionManager:
	Timeout: float
	def ConnectLocal(self, dataModel: DataModel):
		pass

	def ConnectRemote(self, host: str, port: int):
		pass

	def FocusConnection(self, connection: DebuggerConnection):
		pass

	def GetConnectionById(self, id: int):
		pass


	pass

class DebuggerLuaResponse:
	IsError: bool
	IsSuccess: bool
	Message: str
	RequestId: int
	Status: DebuggerStatus
	def GetArg(self):
		pass


	pass

class DebuggerManager:
	DebuggingEnabled: bool
	def AddDebugger(self, script: Instance):
		pass

	def EnableDebugging(self):
		pass

	def GetDebuggers(self):
		pass

	def Resume(self):
		pass

	def StepIn(self):
		pass

	def StepOut(self):
		pass

	def StepOver(self):
		pass


	pass

class DebuggerUIService:
	def EditBreakpoint(self, metaBreakpointId: int):
		pass

	def EditWatch(self, expression: str):
		pass

	def IsConnectionForPlayDataModel(self, debuggerConnectionId: int):
		pass

	def OpenScriptAtLine(self, guid: str, debuggerConnectionId: int, line: int, showErrorOnFail: bool):
		pass

	def Pause(self):
		pass

	def RemoveScriptLineMarkers(self, debuggerConnectionId: int, allMarkers: bool):
		pass

	def Resume(self):
		pass

	def SetCurrentFrameId(self, debuggerThreadId: int, debuggerFrameId: int):
		pass

	def SetCurrentThreadId(self, debuggerThreadId: int):
		pass

	def SetScriptLineMarker(self, guid: str, debuggerConnectionId: int, line: int, lineMarkerType: bool):
		pass


	pass

class DebuggerVariable:
	Name: str
	Populated: bool
	Type: str
	Value: str
	VariableId: int
	VariablesCount: int
	def GetVariableByIndex(self, index: int):
		pass

	def GetVariableByName(self, name: str):
		pass


	pass

class DebuggerWatch:
	Expression: str

	pass

class DeviceIdService:
	def GetDeviceId(self):
		pass


	pass

class Dialog:
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
	def GetCurrentPlayers(self):
		pass

	def SetPlayerIsUsing(self, player: Instance, isUsing: bool):
		pass

	def SignalDialogChoiceSelected(self, player: Instance, dialogChoice: Instance):
		pass


	pass

class DialogChoice:
	GoodbyeChoiceActive: bool
	GoodbyeDialog: str
	ResponseDialog: str
	UserDialog: str

	pass

class DraftsService:
	def DiscardEdits(self, scripts: Objects):
		pass

	def GetDraftStatus(self, script: Instance):
		pass

	def GetEditors(self, script: Instance):
		pass

	def RestoreScripts(self, scripts: Objects):
		pass

	def ShowDiffsAgainstBase(self, scripts: Objects):
		pass

	def ShowDiffsAgainstServer(self, scripts: Objects):
		pass

	def CommitEdits(self, scripts: Objects):
		pass

	def GetDrafts(self):
		pass

	def UpdateToLatestVersion(self, scripts: Objects):
		pass


	pass

class Dragger:
	def AxisRotate(self, axis: Axis):
		pass

	def MouseDown(self, mousePart: Instance, pointOnMousePart: Vector3, parts: Objects):
		pass

	def MouseMove(self, mouseRay: Ray):
		pass

	def MouseUp(self):
		pass


	pass

class DraggerService:
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

class EulerRotationCurve:
	RotationOrder: RotationOrder
	def GetAnglesAtTime(self, time: float):
		pass

	def GetRotationAtTime(self, time: float):
		pass

	def X(self):
		pass

	def Y(self):
		pass

	def Z(self):
		pass


	pass

class EventIngestService:
	def SendEventDeferred(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SendEventImmediately(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SetRBXEvent(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SetRBXEventStream(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass


	pass

class ExperienceInviteOptions:
	InviteMessageId: int
	InviteUser: int
	LaunchData: str
	PromptMessage: str

	pass

class Explosion:
	BlastPressure: float
	BlastRadius: float
	DestroyJointRadiusPercent: float
	Position: Vector3
	TimeScale: float
	Visible: bool
	ExplosionType: ExplosionType

	pass

class FaceAnimatorService:
	AudioAnimationEnabled: bool
	FlipHeadOrientation: bool
	VideoAnimationEnabled: bool
	def GetTrackerLodController(self):
		pass

	def Init(self, videoEnabled: bool, audioEnabled: bool):
		pass

	def IsStarted(self):
		pass

	def Start(self):
		pass

	def Step(self):
		pass

	def Stop(self):
		pass


	pass

class FaceControls:
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

class FaceInstance:
	Face: NormalId

	pass

class Decal:
	LocalTransparencyModifier: float
	Shiny: float
	Specular: float
	Texture: Content
	Transparency: float
	ZIndex: int
	Color3: Color3

	pass

class Texture:
	OffsetStudsU: float
	OffsetStudsV: float
	StudsPerTileU: float
	StudsPerTileV: float

	pass

class FacialAnimationRecordingService:
	BiometricDataConsent: bool
	def IsAgeRestricted(self):
		pass

	def CheckOrRequestCameraPermission(self):
		pass


	pass

class FacialAnimationStreamingService:
	EnableFlags: FacialAnimationFlags
	Enabled: bool

	pass

class FacialAnimationStreamingServiceV2:
	ServiceState: int
	def IsAudioEnabled(self, mask: int):
		pass

	def IsPlaceEnabled(self, mask: int):
		pass

	def IsServerEnabled(self, mask: int):
		pass

	def IsVideoEnabled(self, mask: int):
		pass

	def ResolveStateForUser(self, userId: int):
		pass


	pass

class Feature:
	FaceId: NormalId
	InOut: InOut
	LeftRight: LeftRight
	TopBottom: TopBottom

	pass

class Hole:

	pass

class MotorFeature:

	pass

class File:
	Size: int
	def GetBinaryContents(self):
		pass

	def GetTemporaryId(self):
		pass


	pass

class Fire:
	Color: Color3
	Enabled: bool
	Heat: float
	SecondaryColor: Color3
	Size: float
	TimeScale: float
	size: float
	def FastForward(self, numFrames: int):
		pass


	pass

class FlagStandService:

	pass

class FloatCurve:
	Length: int
	def GetKeyAtIndex(self, index: int):
		pass

	def GetKeyIndicesAtTime(self, time: float):
		pass

	def GetKeys(self):
		pass

	def GetValueAtTime(self, time: float):
		pass

	def InsertKey(self, key: FloatCurveKey):
		pass

	def RemoveKeyAtIndex(self, startingIndex: int, count: int):
		pass

	def SetKeys(self, keys: list[Any]):
		pass


	pass

class FlyweightService:

	pass

class CSGDictionaryService:

	pass

class NonReplicatedCSGDictionaryService:

	pass

class Folder:

	pass

class ForceField:
	Visible: bool

	pass

class FriendService:
	def GetPlatformFriends(self):
		pass


	pass

class FunctionalTest:
	Description: str
	def Error(self, message: str):
		pass

	def Failed(self, message: str):
		pass

	def Pass(self, message: str):
		pass

	def Passed(self, message: str):
		pass

	def Warn(self, message: str):
		pass


	pass

class GamePassService:
	def PlayerHasPass(self, player: Player, gamePassId: int):
		pass


	pass

class GameSettings:
	VideoCaptureEnabled: bool
	VideoRecording: bool

	pass

class GamepadService:
	GamepadCursorEnabled: bool
	def DisableGamepadCursor(self):
		pass

	def EnableGamepadCursor(self, guiObject: Instance):
		pass

	def GetGamepadCursorPosition(self):
		pass

	def SetGamepadCursorPosition(self, position: Vector2):
		pass


	pass

class Geometry:

	pass

class GetTextBoundsParams:
	Size: float
	Text: str
	Width: float
	Font: Font

	pass

class GlobalDataStore:
	def OnUpdate(self, key: str, callback: Callable[..., Any]):
		pass

	def GetAsync(self, key: str):
		pass

	def IncrementAsync(self, key: str, delta: int, userIds: list[Any], options: DataStoreIncrementOptions):
		pass

	def RemoveAsync(self, key: str):
		pass

	def SetAsync(self, key: str, value: Any, userIds: list[Any], options: DataStoreSetOptions):
		pass

	def UpdateAsync(self, key: str, transformFunction: Callable[..., Any]):
		pass


	pass

class DataStore:
	def GetVersionAsync(self, key: str, version: str):
		pass

	def ListKeysAsync(self, prefix: str, pageSize: int, cursor: str):
		pass

	def ListVersionsAsync(self, key: str, sortDirection: SortDirection, minDate: int, maxDate: int, pageSize: int):
		pass

	def RemoveVersionAsync(self, key: str, version: str):
		pass


	pass

class OrderedDataStore:
	def GetSortedAsync(self, ascending: bool, pagesize: int, minValue: Any, maxValue: Any):
		pass


	pass

class GoogleAnalyticsConfiguration:

	pass

class GroupService:
	def GetAlliesAsync(self, groupId: int):
		pass

	def GetEnemiesAsync(self, groupId: int):
		pass

	def GetGroupInfoAsync(self, groupId: int):
		pass

	def GetGroupsAsync(self, userId: int):
		pass


	pass

class GuiBase:

	pass

class GuiBase2d:
	AbsolutePosition: Vector2
	AbsoluteRotation: float
	AbsoluteSize: Vector2
	AutoLocalize: bool
	ClippedRect: Rect
	IsNotOccluded: bool
	Localize: bool
	RawRect2D: Rect
	RootLocalizationTable: LocalizationTable
	SelectionBehaviorDown: SelectionBehavior
	SelectionBehaviorLeft: SelectionBehavior
	SelectionBehaviorRight: SelectionBehavior
	SelectionBehaviorUp: SelectionBehavior
	SelectionGroup: bool
	TotalGroupScale: float

	pass

class GuiObject:
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
	NextSelectionDown: Self
	NextSelectionLeft: Self
	NextSelectionRight: Self
	NextSelectionUp: Self
	Position: UDim2
	Rotation: float
	Selectable: bool
	SelectionImageObject: Self
	SelectionOrder: int
	Size: UDim2
	Transparency: float
	Visible: bool
	ZIndex: int
	AutomaticSize: AutomaticSize
	BorderMode: BorderMode
	SizeConstraint: SizeConstraint
	def TweenPosition(self, endPosition: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]):
		pass

	def TweenSize(self, endSize: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]):
		pass

	def TweenSizeAndPosition(self, endSize: UDim2, endPosition: UDim2, easingDirection: EasingDirection, easingStyle: EasingStyle, time: float, override: bool, callback: Callable[..., Any]):
		pass


	pass

class CanvasGroup:
	GroupColor3: Color3
	GroupTransparency: float

	pass

class Frame:
	Style: FrameStyle

	pass

class GuiButton:
	AutoButtonColor: bool
	Modal: bool
	Selected: bool
	Style: ButtonStyle

	pass

class ImageButton:
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
	def SetEnableContentImageSizeChangedEvents(self, enabled: bool):
		pass


	pass

class TextButton:
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
	def SetTextFromInput(self, text: str):
		pass


	pass

class GuiLabel:

	pass

class ImageLabel:
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
	def SetEnableContentImageSizeChangedEvents(self, enabled: bool):
		pass


	pass

class TextLabel:
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
	def SetTextFromInput(self, text: str):
		pass


	pass

class ScrollingFrame:
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
	def ClearInertialScrolling(self):
		pass

	def GetSampledInertialVelocity(self):
		pass

	def ScrollToTop(self):
		pass


	pass

class TextBox:
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
	def CaptureFocus(self):
		pass

	def IsFocused(self):
		pass

	def ReleaseFocus(self, submitted: bool):
		pass

	def ResetKeyboardMode(self):
		pass

	def SetTextFromInput(self, text: str):
		pass


	pass

class VideoFrame:
	IsLoaded: bool
	Looped: bool
	Playing: bool
	Resolution: Vector2
	TimeLength: float
	TimePosition: float
	Video: Content
	Volume: float
	def Pause(self):
		pass

	def Play(self):
		pass


	pass

class ViewportFrame:
	Ambient: Color3
	CurrentCamera: Camera
	ImageColor3: Color3
	ImageTransparency: float
	IsMirrored: bool
	LightColor: Color3
	LightDirection: Vector3

	pass

class LayerCollector:
	Enabled: bool
	ResetOnSpawn: bool
	ZIndexBehavior: ZIndexBehavior
	def GetLayoutNodeTree(self):
		pass


	pass

class BillboardGui:
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
	def GetScreenSpaceBounds(self):
		pass


	pass

class PluginGui:
	Title: str
	def BindToClose(self, function: Callable[..., Any]):
		pass

	def GetRelativeMousePosition(self):
		pass


	pass

class DockWidgetPluginGui:
	HostWidgetWasRestored: bool
	def RequestRaise(self):
		pass


	pass

class QWidgetPluginGui:

	pass

class ScreenGui:
	ClipToDeviceSafeArea: bool
	DisplayOrder: int
	IgnoreGuiInset: bool
	OnTopOfCoreBlur: bool
	SafeAreaCompatibility: SafeAreaCompatibility

	pass

class GuiMain:

	pass

class SurfaceGuiBase:
	Active: bool
	Adornee: Instance
	Face: NormalId

	pass

class AdGui:
	AdShape: AdShape

	pass

class SurfaceGui:
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

class GuiBase3d:
	Color: BrickColor
	Transparency: float
	Visible: bool
	Color3: Color3

	pass

class FloorWire:
	CycleOffset: float
	From: BasePart
	StudsBetweenTextures: float
	Texture: Content
	TextureSize: Vector2
	To: BasePart
	Velocity: float
	WireRadius: float

	pass

class InstanceAdornment:
	Adornee: Instance

	pass

class SelectionBox:
	LineThickness: float
	SurfaceColor: BrickColor
	SurfaceColor3: Color3
	SurfaceTransparency: float

	pass

class PVAdornment:
	Adornee: PVInstance

	pass

class HandleAdornment:
	AlwaysOnTop: bool
	SizeRelativeOffset: Vector3
	ZIndex: int
	AdornCullingMode: AdornCullingMode
	CFrame: CFrame

	pass

class BoxHandleAdornment:
	Size: Vector3

	pass

class ConeHandleAdornment:
	Height: float
	Radius: float

	pass

class CylinderHandleAdornment:
	Angle: float
	Height: float
	InnerRadius: float
	Radius: float

	pass

class ImageHandleAdornment:
	Image: Content
	Size: Vector2

	pass

class LineHandleAdornment:
	Length: float
	Thickness: float

	pass

class SphereHandleAdornment:
	Radius: float

	pass

class WireframeHandleAdornment:
	def AddLine(self, from: Vector3, to: Vector3):
		pass

	def AddLines(self, points: list[Any]):
		pass

	def AddPath(self, points: list[Any], loop: bool):
		pass

	def Clear(self):
		pass


	pass

class ParabolaAdornment:
	A: float
	B: float
	C: float
	Range: float
	Thickness: float
	def FindPartOnParabola(self, ignoreDescendentsTable: Objects):
		pass


	pass

class SelectionSphere:
	SurfaceColor: BrickColor
	SurfaceColor3: Color3
	SurfaceTransparency: float

	pass

class PartAdornment:
	Adornee: BasePart

	pass

class HandlesBase:

	pass

class ArcHandles:
	Axes: Axes

	pass

class Handles:
	Style: HandlesStyle
	Faces: Faces

	pass

class SurfaceSelection:
	TargetSurface: NormalId

	pass

class SelectionLasso:
	Humanoid: Humanoid

	pass

class SelectionPartLasso:
	Part: BasePart

	pass

class SelectionPointLasso:
	Point: Vector3

	pass

class GuiService:
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
	def AddCenterDialog(self, dialog: Instance, centerDialogType: CenterDialogType, showFunction: Callable[..., Any], hideFunction: Callable[..., Any]):
		pass

	def AddKey(self, key: str):
		pass

	def AddSelectionParent(self, selectionName: str, selectionParent: Instance):
		pass

	def AddSelectionTuple(self, selectionName: str, selections: tuple[Any]):
		pass

	def AddSpecialKey(self, key: SpecialKey):
		pass

	def BroadcastNotification(self, data: str, notificationType: int):
		pass

	def ClearError(self):
		pass

	def CloseInspectMenu(self):
		pass

	def CloseStatsBasedOnInputString(self, input: str):
		pass

	def ForceTenFootInterface(self, isForced: bool):
		pass

	def GetBrickCount(self):
		pass

	def GetClosestDialogToPosition(self, position: Vector3):
		pass

	def GetEmotesMenuOpen(self):
		pass

	def GetErrorCode(self):
		pass

	def GetErrorMessage(self):
		pass

	def GetErrorType(self):
		pass

	def GetGameplayPausedNotificationEnabled(self):
		pass

	def GetGuiInset(self):
		pass

	def GetGuiIsVisible(self, guiType: GuiType):
		pass

	def GetInspectMenuEnabled(self):
		pass

	def GetNotificationTypeList(self):
		pass

	def GetResolutionScale(self):
		pass

	def GetSafeZoneOffsets(self):
		pass

	def GetUiMessage(self):
		pass

	def InspectPlayerFromHumanoidDescription(self, humanoidDescription: Instance, name: str):
		pass

	def InspectPlayerFromUserId(self, userId: int):
		pass

	def InspectPlayerFromUserIdWithCtx(self, userId: int, ctx: str):
		pass

	def IsMemoryTrackerEnabled(self):
		pass

	def IsTenFootInterface(self):
		pass

	def OpenBrowserWindow(self, url: str):
		pass

	def OpenNativeOverlay(self, title: str, url: str):
		pass

	def RemoveCenterDialog(self, dialog: Instance):
		pass

	def RemoveKey(self, key: str):
		pass

	def RemoveSelectionGroup(self, selectionName: str):
		pass

	def RemoveSpecialKey(self, key: SpecialKey):
		pass

	def Select(self, selectionParent: Instance):
		pass

	def SetEmotesMenuOpen(self, isOpen: bool):
		pass

	def SetGameplayPausedNotificationEnabled(self, enabled: bool):
		pass

	def SetGlobalGuiInset(self, x1: int, y1: int, x2: int, y2: int):
		pass

	def SetHardwareSafeAreaInsets(self, left: float, top: float, right: float, bottom: float):
		pass

	def SetInspectMenuEnabled(self, enabled: bool):
		pass

	def SetMenuIsOpen(self, open: bool, menuName: str):
		pass

	def SetSafeZoneOffsets(self, top: float, bottom: float, left: float, right: float):
		pass

	def SetUiMessage(self, msgType: UiMessageType, uiMessage: str):
		pass

	def ShowStatsBasedOnInputString(self, input: str):
		pass

	def ToggleFullscreen(self):
		pass

	def ToggleGuiIsVisibleIfAllowed(self, guiType: GuiType):
		pass

	def GetScreenResolution(self):
		pass


	pass

class GuidRegistryService:

	pass

class HapticService:
	def GetMotor(self, inputType: UserInputType, vibrationMotor: VibrationMotor):
		pass

	def IsMotorSupported(self, inputType: UserInputType, vibrationMotor: VibrationMotor):
		pass

	def IsVibrationSupported(self, inputType: UserInputType):
		pass

	def SetMotor(self, inputType: UserInputType, vibrationMotor: VibrationMotor, vibrationValues: tuple[Any]):
		pass


	pass

class HeightmapImporterService:
	def CancelImportHeightmap(self):
		pass

	def IsValidColormap(self, colormapAssetId: Content):
		pass

	def IsValidHeightmap(self, heightmapAssetId: Content):
		pass

	def SetImportHeightmapPaused(self, paused: bool):
		pass

	def GetHeightmapPreviewAsync(self, heightmapAssetId: Content):
		pass

	def ImportHeightmap(self, region: Region3, heightmapAssetId: Content, colormapAssetId: Content, defaultMaterial: Material):
		pass


	pass

class HiddenSurfaceRemovalAsset:

	pass

class Highlight:
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

class Hopper:

	pass

class HttpRbxApiService:
	def GetDocumentationUrl(self, partialUrl: str):
		pass

	def GetAsync(self, apiUrlPath: str, priority: ThrottlingPriority, httpRequestType: HttpRequestType):
		pass

	def GetAsyncFullUrl(self, apiUrl: str, priority: ThrottlingPriority, httpRequestType: HttpRequestType):
		pass

	def PostAsync(self, apiUrlPath: str, data: str, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType):
		pass

	def PostAsyncFullUrl(self, apiUrl: str, data: str, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType):
		pass

	def RequestAsync(self, requestOptions: Dictionary, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType):
		pass

	def RequestLimitedAsync(self, requestOptions: Dictionary, priority: ThrottlingPriority, content_type: HttpContentType, httpRequestType: HttpRequestType):
		pass


	pass

class HttpRequest:
	def Cancel(self):
		pass

	def Start(self, callback: Callable[..., Any]):
		pass


	pass

class HttpService:
	HttpEnabled: bool
	def GenerateGUID(self, wrapInCurlyBraces: bool):
		pass

	def GetHttpEnabled(self):
		pass

	def GetUserAgent(self):
		pass

	def JSONDecode(self, input: str):
		pass

	def JSONEncode(self, input: Any):
		pass

	def RequestInternal(self, options: Dictionary):
		pass

	def SetHttpEnabled(self, enabled: bool):
		pass

	def UrlEncode(self, input: str):
		pass

	def GetAsync(self, url: str, nocache: bool, headers: Any):
		pass

	def PostAsync(self, url: str, data: str, content_type: HttpContentType, compress: bool, headers: Any):
		pass

	def RequestAsync(self, requestOptions: Dictionary):
		pass


	pass

class Humanoid:
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
	LeftLeg: BasePart
	MaxHealth: float
	MaxSlopeAngle: float
	MoveDirection: Vector3
	NameDisplayDistance: float
	PlatformStand: bool
	RequiresNeck: bool
	RigType: HumanoidRigType
	RightLeg: BasePart
	RootPart: BasePart
	SeatPart: BasePart
	Sit: bool
	TargetPoint: Vector3
	Torso: BasePart
	UseJumpPower: bool
	WalkSpeed: float
	WalkToPart: BasePart
	WalkToPoint: Vector3
	maxHealth: float
	NameOcclusion: NameOcclusion
	def AddAccessory(self, accessory: Instance):
		pass

	def AddCustomStatus(self, status: str):
		pass

	def AddStatus(self, status: Status):
		pass

	def ApplyDescriptionBlocking(self, humanoidDescription: HumanoidDescription):
		pass

	def BuildRigFromAttachments(self):
		pass

	def CacheDefaults(self):
		pass

	def ChangeState(self, state: HumanoidStateType):
		pass

	def EquipTool(self, tool: Instance):
		pass

	def GetAccessories(self):
		pass

	def GetAccessoryHandleScale(self, instance: Instance, partType: BodyPartR15):
		pass

	def GetAppliedDescription(self):
		pass

	def GetBodyPartR15(self, part: Instance):
		pass

	def GetLimb(self, part: Instance):
		pass

	def GetPlayingAnimationTracks(self):
		pass

	def GetState(self):
		pass

	def GetStateEnabled(self, state: HumanoidStateType):
		pass

	def GetStatuses(self):
		pass

	def HasCustomStatus(self, status: str):
		pass

	def HasStatus(self, status: Status):
		pass

	def LoadAnimation(self, animation: Animation):
		pass

	def Move(self, moveDirection: Vector3, relativeToCamera: bool):
		pass

	def MoveTo(self, location: Vector3, part: Instance):
		pass

	def RemoveAccessories(self):
		pass

	def RemoveCustomStatus(self, status: str):
		pass

	def RemoveStatus(self, status: Status):
		pass

	def ReplaceBodyPartR15(self, bodyPart: BodyPartR15, part: BasePart):
		pass

	def SetClickToWalkEnabled(self, enabled: bool):
		pass

	def SetStateEnabled(self, state: HumanoidStateType, enabled: bool):
		pass

	def TakeDamage(self, amount: float):
		pass

	def UnequipTools(self):
		pass

	def loadAnimation(self, animation: Animation):
		pass

	def takeDamage(self, amount: float):
		pass

	def ApplyDescription(self, humanoidDescription: HumanoidDescription, assetTypeVerification: AssetTypeVerification):
		pass

	def ApplyDescriptionClientServer(self, humanoidDescription: HumanoidDescription):
		pass

	def ApplyDescriptionReset(self, humanoidDescription: HumanoidDescription, assetTypeVerification: AssetTypeVerification):
		pass

	def PlayEmote(self, emoteName: str):
		pass

	def PlayEmoteAndGetAnimTrackById(self, emoteId: int):
		pass


	pass

class HumanoidDescription:
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
	def AddEmote(self, name: str, assetId: int):
		pass

	def GetAccessories(self, includeRigidAccessories: bool):
		pass

	def GetEmotes(self):
		pass

	def GetEquippedEmotes(self):
		pass

	def RemoveEmote(self, name: str):
		pass

	def SetAccessories(self, accessories: list[Any], includeRigidAccessories: bool):
		pass

	def SetEmotes(self, emotes: Dictionary):
		pass

	def SetEquippedEmotes(self, equippedEmotes: list[Any]):
		pass


	pass

class IKControl:
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

class ILegacyStudioBridge:

	pass

class LegacyStudioBridge:

	pass

class IXPService:
	def ClearUserLayers(self):
		pass

	def GetBrowserTrackerLayerLoadingStatus(self):
		pass

	def GetBrowserTrackerLayerVariables(self, layerName: str):
		pass

	def GetBrowserTrackerStatusForLayer(self, layerName: str):
		pass

	def GetRegisteredUserLayersToStatus(self):
		pass

	def GetUserLayerLoadingStatus(self):
		pass

	def GetUserLayerVariables(self, layerName: str):
		pass

	def GetUserStatusForLayer(self, layerName: str):
		pass

	def InitializeUserLayers(self, userId: int):
		pass

	def LogBrowserTrackerLayerExposure(self, layerName: str):
		pass

	def LogUserLayerExposure(self, layerName: str):
		pass

	def RegisterUserLayers(self, userLayers: Any):
		pass


	pass

class ImporterBaseSettings:
	Id: str
	ImportName: str
	ShouldImport: bool
	def GetStatuses(self):
		pass


	pass

class ImporterAnimationSettings:

	pass

class ImporterFacsSettings:

	pass

class ImporterGroupSettings:
	Anchored: bool
	ImportAsModelAsset: bool
	InsertInWorkspace: bool

	pass

class ImporterJointSettings:

	pass

class ImporterMaterialSettings:
	DiffuseFilePath: str
	IsPbr: bool
	MetalnessFilePath: str
	NormalFilePath: str
	RoughnessFilePath: str

	pass

class ImporterMeshSettings:
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

class ImporterRootSettings:
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

class IncrementalPatchBuilder:
	HighCompression: bool
	ZstdCompression: bool

	pass

class InputObject:
	Delta: Vector3
	Position: Vector3
	KeyCode: KeyCode
	UserInputState: UserInputState
	UserInputType: UserInputType
	def IsModifierKeyDown(self, modifierKey: ModifierKey):
		pass


	pass

class InsertService:
	AllowClientInsertModels: bool
	AllowInsertFreeModels: bool
	def ApproveAssetId(self, assetId: int):
		pass

	def ApproveAssetVersionId(self, assetVersionId: int):
		pass

	def Insert(self, instance: Instance):
		pass

	def LoadLocalAsset(self, assetPath: str):
		pass

	def LoadPackageAsset(self, url: Content):
		pass

	def CreateMeshPartAsync(self, meshId: Content, collisionFidelity: CollisionFidelity, renderFidelity: RenderFidelity):
		pass

	def GetBaseCategories(self):
		pass

	def GetBaseSets(self):
		pass

	def GetCollection(self, categoryId: int):
		pass

	def GetFreeDecals(self, searchText: str, pageNum: int):
		pass

	def GetFreeModels(self, searchText: str, pageNum: int):
		pass

	def GetLatestAssetVersionAsync(self, assetId: int):
		pass

	def GetUserCategories(self, userId: int):
		pass

	def GetUserSets(self, userId: int):
		pass

	def LoadAsset(self, assetId: int):
		pass

	def LoadAssetVersion(self, assetVersionId: int):
		pass

	def LoadPackageAssetAsync(self, url: Content):
		pass

	def loadAsset(self, assetId: int):
		pass


	pass

class JointInstance:
	Active: bool
	C0: CFrame
	C1: CFrame
	Enabled: bool
	Part0: BasePart
	Part1: BasePart
	part1: BasePart

	pass

class DynamicRotate:
	BaseAngle: float

	pass

class RotateP:

	pass

class RotateV:

	pass

class Glue:
	F0: Vector3
	F1: Vector3
	F2: Vector3
	F3: Vector3

	pass

class ManualSurfaceJointInstance:

	pass

class ManualGlue:

	pass

class ManualWeld:

	pass

class Motor:
	CurrentAngle: float
	DesiredAngle: float
	MaxVelocity: float
	def SetDesiredAngle(self, value: float):
		pass


	pass

class Motor6D:
	ChildName: str
	ParentName: str
	Transform: CFrame

	pass

class Rotate:

	pass

class Snap:

	pass

class VelocityMotor:
	CurrentAngle: float
	DesiredAngle: float
	MaxVelocity: float
	Hole: Hole

	pass

class Weld:

	pass

class JointsService:
	def ClearJoinAfterMoveJoints(self):
		pass

	def CreateJoinAfterMoveJoints(self):
		pass

	def SetJoinAfterMoveInstance(self, joinInstance: Instance):
		pass

	def SetJoinAfterMoveTarget(self, joinTarget: Instance):
		pass

	def ShowPermissibleJoints(self):
		pass


	pass

class KeyboardService:

	pass

class Keyframe:
	Time: float
	def AddMarker(self, marker: Instance):
		pass

	def AddPose(self, pose: Instance):
		pass

	def GetMarkers(self):
		pass

	def GetPoses(self):
		pass

	def RemoveMarker(self, marker: Instance):
		pass

	def RemovePose(self, pose: Instance):
		pass


	pass

class KeyframeMarker:
	Value: str

	pass

class KeyframeSequenceProvider:
	def GetKeyframeSequence(self, assetId: Content):
		pass

	def GetKeyframeSequenceById(self, assetId: int, useCache: bool):
		pass

	def GetMemStats(self):
		pass

	def RegisterActiveKeyframeSequence(self, keyframeSequence: Instance):
		pass

	def RegisterKeyframeSequence(self, keyframeSequence: Instance):
		pass

	def GetAnimations(self, userId: int):
		pass

	def GetKeyframeSequenceAsync(self, assetId: Content):
		pass


	pass

class LSPFileSyncService:

	pass

class LanguageService:

	pass

class Light:
	Brightness: float
	Color: Color3
	Enabled: bool
	Shadows: bool

	pass

class PointLight:
	Range: float

	pass

class SpotLight:
	Angle: float
	Face: NormalId
	Range: float

	pass

class SurfaceLight:
	Angle: float
	Face: NormalId
	Range: float

	pass

class Lighting:
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
	def GetMinutesAfterMidnight(self):
		pass

	def GetMoonDirection(self):
		pass

	def GetMoonPhase(self):
		pass

	def GetSunDirection(self):
		pass

	def SetMinutesAfterMidnight(self, minutes: float):
		pass

	def getMinutesAfterMidnight(self):
		pass

	def setMinutesAfterMidnight(self, minutes: float):
		pass


	pass

class LocalStorageService:
	def Flush(self):
		pass

	def GetItem(self, key: str):
		pass

	def SetItem(self, key: str, value: str):
		pass

	def WhenLoaded(self, callback: Callable[..., Any]):
		pass


	pass

class AppStorageService:

	pass

class UserStorageService:

	pass

class LocalizationService:
	ForcePlayModeGameLocaleId: str
	ForcePlayModeRobloxLocaleId: str
	IsTextScraperRunning: bool
	RobloxForcePlayModeGameLocaleId: str
	RobloxForcePlayModeRobloxLocaleId: str
	RobloxLocaleId: str
	SystemLocaleId: str
	def GetCorescriptLocalizations(self):
		pass

	def GetTableEntries(self, instance: Instance):
		pass

	def GetTranslatorForPlayer(self, player: Instance):
		pass

	def SetRobloxLocaleId(self, locale: str):
		pass

	def StartTextScraper(self):
		pass

	def StopTextScraper(self):
		pass

	def GetCountryRegionForPlayerAsync(self, player: Instance):
		pass

	def GetTranslatorForLocaleAsync(self, locale: str):
		pass

	def GetTranslatorForPlayerAsync(self, player: Instance):
		pass

	def PromptDownloadGameTableToCSV(self, table: Instance):
		pass

	def PromptExportToCSVs(self):
		pass

	def PromptImportFromCSVs(self):
		pass

	def PromptUploadCSVToGameTable(self):
		pass


	pass

class LocalizationTable:
	DevelopmentLanguage: str
	Root: Instance
	SourceLocaleId: str
	def GetContents(self):
		pass

	def GetEntries(self):
		pass

	def GetString(self, targetLocaleId: str, key: str):
		pass

	def GetTranslator(self, localeId: str):
		pass

	def RemoveEntry(self, key: str, source: str, context: str):
		pass

	def RemoveEntryValue(self, key: str, source: str, context: str, localeId: str):
		pass

	def RemoveKey(self, key: str):
		pass

	def RemoveTargetLocale(self, localeId: str):
		pass

	def SetContents(self, contents: str):
		pass

	def SetEntries(self, entries: Any):
		pass

	def SetEntry(self, key: str, targetLocaleId: str, text: str):
		pass

	def SetEntryContext(self, key: str, source: str, context: str, newContext: str):
		pass

	def SetEntryExample(self, key: str, source: str, context: str, example: str):
		pass

	def SetEntryKey(self, key: str, source: str, context: str, newKey: str):
		pass

	def SetEntrySource(self, key: str, source: str, context: str, newSource: str):
		pass

	def SetEntryValue(self, key: str, source: str, context: str, localeId: str, text: str):
		pass

	def SetIsExemptFromUGCAnalytics(self, value: bool):
		pass


	pass

class CloudLocalizationTable:

	pass

class LodDataEntity:
	EntityLodEnabled: bool

	pass

class LodDataService:

	pass

class LogService:
	def ExecuteScript(self, source: str):
		pass

	def GetHttpResultHistory(self):
		pass

	def GetLogHistory(self):
		pass

	def RequestHttpResultApproved(self):
		pass

	def RequestServerHttpResult(self):
		pass

	def RequestServerOutput(self):
		pass


	pass

class LoginService:
	def Logout(self):
		pass

	def PromptLogin(self):
		pass


	pass

class LuaSettings:

	pass

class LuaSourceContainer:
	CurrentEditor: Instance

	pass

class BaseScript:
	Disabled: bool
	Enabled: bool
	LinkedSource: Content
	RunContext: RunContext

	pass

class CoreScript:

	pass

class Script:
	Source: ProtectedString
	def GetHash(self):
		pass


	pass

class LocalScript:

	pass

class ModuleScript:
	LinkedSource: Content
	Source: ProtectedString

	pass

class LuaWebService:

	pass

class LuauScriptAnalyzerService:

	pass

class MarkerCurve:
	Length: int
	def GetMarkerAtIndex(self, index: int):
		pass

	def GetMarkers(self):
		pass

	def InsertMarkerAtTime(self, time: float, marker: str):
		pass

	def RemoveMarkerAtIndex(self, startingIndex: int, count: int):
		pass


	pass

class MarketplaceService:
	def PlayerCanMakePurchases(self, player: Instance):
		pass

	def PromptBundlePurchase(self, player: Instance, bundleId: int):
		pass

	def PromptGamePassPurchase(self, player: Instance, gamePassId: int):
		pass

	def PromptNativePurchase(self, player: Instance, productId: str):
		pass

	def PromptNativePurchaseWithLocalPlayer(self, productId: str):
		pass

	def PromptPremiumPurchase(self, player: Instance):
		pass

	def PromptProductPurchase(self, player: Instance, productId: int, equipIfPurchased: bool, currencyType: CurrencyType):
		pass

	def PromptPurchase(self, player: Instance, assetId: int, equipIfPurchased: bool, currencyType: CurrencyType):
		pass

	def PromptRobloxPurchase(self, assetId: int, equipIfPurchased: bool):
		pass

	def PromptSubscriptionCancellation(self, player: Instance, subscriptionId: int):
		pass

	def PromptSubscriptionPurchase(self, player: Instance, subscriptionId: int):
		pass

	def PromptThirdPartyPurchase(self, player: Instance, productId: str):
		pass

	def ReportAssetSale(self, assetId: str, robuxAmount: int):
		pass

	def ReportRobuxUpsellStarted(self):
		pass

	def SignalAssetTypePurchased(self, player: Instance, assetType: AssetType):
		pass

	def SignalClientPurchaseSuccess(self, ticket: str, playerId: int, productId: int):
		pass

	def SignalMockPurchasePremium(self):
		pass

	def SignalPromptBundlePurchaseFinished(self, player: Instance, bundleId: int, success: bool):
		pass

	def SignalPromptGamePassPurchaseFinished(self, player: Instance, gamePassId: int, success: bool):
		pass

	def SignalPromptPremiumPurchaseFinished(self, didTryPurchasing: bool):
		pass

	def SignalPromptProductPurchaseFinished(self, userId: int, productId: int, success: bool):
		pass

	def SignalPromptPurchaseFinished(self, player: Instance, assetId: int, success: bool):
		pass

	def SignalPromptSubscriptionCancellationFinished(self, player: Instance, subscriptionId: int, wasCanceled: bool):
		pass

	def SignalPromptSubscriptionPurchaseFinished(self, player: Instance, subscriptionId: int, wasPurchased: bool):
		pass

	def SignalServerLuaDialogClosed(self, value: bool):
		pass

	def GetDeveloperProductsAsync(self):
		pass

	def GetProductInfo(self, assetId: int, infoType: InfoType):
		pass

	def GetRobuxBalance(self):
		pass

	def IsPlayerSubscribed(self, player: Instance, subscriptionId: int):
		pass

	def PerformPurchase(self, infoType: InfoType, productId: int, expectedPrice: int, requestId: str, isRobloxPurchase: bool):
		pass

	def PlayerOwnsAsset(self, player: Instance, assetId: int):
		pass

	def PlayerOwnsBundle(self, player: Player, bundleId: int):
		pass

	def UserOwnsGamePassAsync(self, userId: int, gamePassId: int):
		pass


	pass

class MaterialService:
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
	def GetBaseMaterialOverride(self, material: Material):
		pass

	def GetMaterialOverrideChanged(self, material: Material):
		pass

	def GetMaterialVariant(self, material: Material, name: str):
		pass

	def GetOverrideStatus(self, material: Material):
		pass

	def SetBaseMaterialOverride(self, material: Material, name: str):
		pass


	pass

class MaterialVariant:
	BaseMaterial: Material
	ColorMap: Content
	CustomPhysicalProperties: PhysicalProperties
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	StudsPerTile: float
	MaterialPattern: MaterialPattern

	pass

class MemStorageConnection:
	def Disconnect(self):
		pass


	pass

class MemStorageService:
	def Bind(self, key: str, callback: Callable[..., Any]):
		pass

	def BindAndFire(self, key: str, callback: Callable[..., Any]):
		pass

	def Call(self, key: str, input: Any):
		pass

	def Fire(self, key: str, value: str):
		pass

	def GetItem(self, key: str, defaultValue: str):
		pass

	def HasItem(self, key: str):
		pass

	def RemoveItem(self, key: str):
		pass

	def SetItem(self, key: str, value: str):
		pass


	pass

class MemoryStoreQueue:
	def AddAsync(self, value: Any, expiration: int, priority: float):
		pass

	def ReadAsync(self, count: int, allOrNothing: bool, waitTimeout: float):
		pass

	def RemoveAsync(self, id: str):
		pass


	pass

class MemoryStoreService:
	def GetQueue(self, name: str, invisibilityTimeout: int):
		pass

	def GetSortedMap(self, name: str):
		pass


	pass

class MemoryStoreSortedMap:
	def GetAsync(self, key: str):
		pass

	def GetRangeAsync(self, direction: SortDirection, count: int, exclusiveLowerBound: str, exclusiveUpperBound: str):
		pass

	def RemoveAsync(self, key: str):
		pass

	def SetAsync(self, key: str, value: Any, expiration: int):
		pass

	def UpdateAsync(self, key: str, transformFunction: Callable[..., Any], expiration: int):
		pass


	pass

class Message:
	Text: str

	pass

class Hint:

	pass

class MessageBusConnection:
	def Disconnect(self):
		pass


	pass

class MessageBusService:
	def Call(self, key: str, input: Any):
		pass

	def GetLast(self, mid: str):
		pass

	def GetMessageId(self, domainName: str, messageName: str):
		pass

	def GetProtocolMethodRequestMessageId(self, protocolName: str, methodName: str):
		pass

	def GetProtocolMethodResponseMessageId(self, protocolName: str, methodName: str):
		pass

	def Publish(self, mid: str, params: Any):
		pass

	def PublishProtocolMethodRequest(self, protocolName: str, methodName: str, message: Any, customTelemetryData: Any):
		pass

	def PublishProtocolMethodResponse(self, protocolName: str, methodName: str, message: Any, responseCode: int, customTelemetryData: Any):
		pass

	def Subscribe(self, mid: str, callback: Callable[..., Any], once: bool, sticky: bool):
		pass

	def SubscribeToProtocolMethodRequest(self, protocolName: str, methodName: str, callback: Callable[..., Any], once: bool, sticky: bool):
		pass

	def SubscribeToProtocolMethodResponse(self, protocolName: str, methodName: str, callback: Callable[..., Any], once: bool, sticky: bool):
		pass


	pass

class MessagingService:
	def PublishAsync(self, topic: str, message: Any):
		pass

	def SubscribeAsync(self, topic: str, callback: Callable[..., Any]):
		pass


	pass

class MetaBreakpoint:
	Condition: str
	ContinueExecution: bool
	Enabled: bool
	Id: int
	IsLogpoint: bool
	Line: int
	LogMessage: str
	Script: str
	Valid: bool
	def GetContextBreakpoints(self):
		pass

	def Remove(self, status: Callable[..., Any]):
		pass

	def SetChildBreakpointEnabledByScriptAndContext(self, script: str, contextGST: int, enabled: bool):
		pass

	def SetContextEnabled(self, context: int, enabled: bool):
		pass

	def SetContinueExecution(self, enabled: bool):
		pass

	def SetEnabled(self, enabled: bool):
		pass

	def SetLine(self, line: int, status: Callable[..., Any]):
		pass


	pass

class MetaBreakpointContext:

	pass

class MetaBreakpointManager:
	def AddBreakpoint(self, script: Instance, line: int, condition: Instance):
		pass

	def GetBreakpointById(self, metaBreakpointId: int):
		pass

	def RemoveBreakpointById(self, metaBreakpointId: int):
		pass


	pass

class Mouse:
	Hit: CFrame
	Icon: Content
	Origin: CFrame
	Target: BasePart
	TargetFilter: Instance
	TargetSurface: NormalId
	UnitRay: Ray
	ViewSizeX: int
	ViewSizeY: int
	X: int
	Y: int
	hit: CFrame
	target: BasePart

	pass

class PlayerMouse:

	pass

class PluginMouse:

	pass

class MouseService:

	pass

class MultipleDocumentInterfaceInstance:
	FocusedDataModelSession: Instance

	pass

class NetworkMarker:

	pass

class NetworkPeer:
	def SetOutgoingKBPSLimit(self, limit: int):
		pass


	pass

class NetworkClient:

	pass

class NetworkServer:
	def EncryptStringForPlayerId(self, toEncrypt: str, playerId: int):
		pass


	pass

class NetworkReplicator:
	def GetPlayer(self):
		pass


	pass

class ClientReplicator:
	def RequestRCCProfilerData(self, frameRate: int, timeFrame: int):
		pass

	def RequestServerScriptProfiling(self, start: bool):
		pass

	def RequestServerStats(self, request: bool):
		pass


	pass

class ServerReplicator:

	pass

class NetworkSettings:
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

class NoCollisionConstraint:
	Enabled: bool
	Part0: BasePart
	Part1: BasePart

	pass

class NotificationService:
	IsConnected: bool
	IsLuaChatEnabled: bool
	IsLuaGameDetailsEnabled: bool
	SelectedTheme: str
	def ActionEnabled(self, actionType: AppShellActionType):
		pass

	def ActionTaken(self, actionType: AppShellActionType):
		pass

	def CancelAllNotification(self, userId: int):
		pass

	def CancelNotification(self, userId: int, alertId: int):
		pass

	def ScheduleNotification(self, userId: int, alertId: int, alertMsg: str, minutesToFire: int):
		pass

	def SwitchedToAppShellFeature(self, appShellFeature: AppShellFeature):
		pass

	def GetScheduledNotifications(self, userId: int):
		pass


	pass

class PVInstance:
	OriginOrientation: Vector3
	OriginPosition: Vector3
	PivotOffsetOrientation: Vector3
	PivotOffsetPosition: Vector3
	def GetPivot(self):
		pass

	def PivotTo(self, targetCFrame: CFrame):
		pass


	pass

class BasePart:
	Anchored: bool
	AssemblyAngularVelocity: Vector3
	AssemblyCenterOfMass: Vector3
	AssemblyLinearVelocity: Vector3
	AssemblyMass: float
	AssemblyRootPart: Self
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
	def ApplyAngularImpulse(self, impulse: Vector3):
		pass

	def ApplyImpulse(self, impulse: Vector3):
		pass

	def ApplyImpulseAtPosition(self, impulse: Vector3, position: Vector3):
		pass

	def BreakJoints(self):
		pass

	def CanCollideWith(self, part: Self):
		pass

	def CanSetNetworkOwnership(self):
		pass

	def GetConnectedParts(self, recursive: bool):
		pass

	def GetJoints(self):
		pass

	def GetMass(self):
		pass

	def GetNetworkOwner(self):
		pass

	def GetNetworkOwnershipAuto(self):
		pass

	def GetRenderCFrame(self):
		pass

	def GetRootPart(self):
		pass

	def GetTouchingParts(self):
		pass

	def GetVelocityAtPosition(self, position: Vector3):
		pass

	def IsGrounded(self):
		pass

	def MakeJoints(self):
		pass

	def Resize(self, normalId: NormalId, deltaAmount: int):
		pass

	def SetNetworkOwner(self, playerInstance: Player):
		pass

	def SetNetworkOwnershipAuto(self):
		pass

	def breakJoints(self):
		pass

	def getMass(self):
		pass

	def makeJoints(self):
		pass

	def resize(self, normalId: NormalId, deltaAmount: int):
		pass

	def SubtractAsync(self, parts: Objects, collisionfidelity: CollisionFidelity, renderFidelity: RenderFidelity):
		pass

	def UnionAsync(self, parts: Objects, collisionfidelity: CollisionFidelity, renderFidelity: RenderFidelity):
		pass


	pass

class CornerWedgePart:

	pass

class FormFactorPart:
	formFactor: FormFactor
	FormFactor: FormFactor

	pass

class Part:
	Shape: PartType

	pass

class FlagStand:
	TeamColor: BrickColor

	pass

class Platform:

	pass

class Seat:
	Disabled: bool
	Occupant: Humanoid
	def Sit(self, humanoid: Instance):
		pass


	pass

class SkateboardPlatform:
	Controller: SkateboardController
	ControllingHumanoid: Humanoid
	Steer: int
	StickyWheels: bool
	Throttle: int
	def ApplySpecificImpulse(self, impulseWorld: Vector3):
		pass


	pass

class SpawnLocation:
	AllowTeamChangeOnTouch: bool
	Duration: int
	Enabled: bool
	Neutral: bool
	TeamColor: BrickColor

	pass

class WedgePart:

	pass

class Terrain:
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
	def AutowedgeCell(self, x: int, y: int, z: int):
		pass

	def AutowedgeCells(self, region: Region3int16):
		pass

	def CellCenterToWorld(self, x: int, y: int, z: int):
		pass

	def CellCornerToWorld(self, x: int, y: int, z: int):
		pass

	def Clear(self):
		pass

	def ConvertToSmooth(self):
		pass

	def CopyRegion(self, region: Region3int16):
		pass

	def CountCells(self):
		pass

	def FillBall(self, center: Vector3, radius: float, material: Material):
		pass

	def FillBlock(self, cframe: CFrame, size: Vector3, material: Material):
		pass

	def FillCylinder(self, cframe: CFrame, height: float, radius: float, material: Material):
		pass

	def FillRegion(self, region: Region3, resolution: float, material: Material):
		pass

	def FillWedge(self, cframe: CFrame, size: Vector3, material: Material):
		pass

	def GetCell(self, x: int, y: int, z: int):
		pass

	def GetMaterialColor(self, material: Material):
		pass

	def GetWaterCell(self, x: int, y: int, z: int):
		pass

	def HideTerrainRegion(self):
		pass

	def PasteRegion(self, region: TerrainRegion, corner: Vector3int16, pasteEmptyCells: bool):
		pass

	def ReadVoxels(self, region: Region3, resolution: float):
		pass

	def ReplaceMaterial(self, region: Region3, resolution: float, sourceMaterial: Material, targetMaterial: Material):
		pass

	def SetCell(self, x: int, y: int, z: int, material: CellMaterial, block: CellBlock, orientation: CellOrientation):
		pass

	def SetCells(self, region: Region3int16, material: CellMaterial, block: CellBlock, orientation: CellOrientation):
		pass

	def SetMaterialColor(self, material: Material, value: Color3):
		pass

	def SetTerrainRegion(self, cframe: CFrame, size: Vector3):
		pass

	def SetWaterCell(self, x: int, y: int, z: int, force: WaterForce, direction: WaterDirection):
		pass

	def SetWireframeRegion(self, cframe: CFrame, size: Vector3):
		pass

	def ShowTerrainRegion(self):
		pass

	def WorldToCell(self, position: Vector3):
		pass

	def WorldToCellPreferEmpty(self, position: Vector3):
		pass

	def WorldToCellPreferSolid(self, position: Vector3):
		pass

	def WriteVoxels(self, region: Region3, resolution: float, materials: list[Any], occupancy: list[Any]):
		pass


	pass

class TriangleMeshPart:
	MeshSize: Vector3
	CollisionFidelity: CollisionFidelity

	pass

class MeshPart:
	DoubleSided: bool
	HasJointOffset: bool
	HasSkinnedMesh: bool
	JointOffset: Vector3
	MeshId: Content
	TextureID: Content
	RenderFidelity: RenderFidelity
	def ApplyMesh(self, meshPart: Instance):
		pass


	pass

class PartOperation:
	SmoothingAngle: float
	TriangleCount: int
	UsePartColor: bool
	RenderFidelity: RenderFidelity

	pass

class NegateOperation:

	pass

class UnionOperation:

	pass

class TrussPart:
	Style: Style

	pass

class VehicleSeat:
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
	def Sit(self, humanoid: Instance):
		pass


	pass

class Model:
	LevelOfDetail: ModelLevelOfDetail
	PrimaryPart: BasePart
	WorldPivotOrientation: Vector3
	WorldPivotPosition: Vector3
	WorldPivot: CFrame
	ModelStreamingMode: ModelStreamingMode
	def BreakJoints(self):
		pass

	def GetBoundingBox(self):
		pass

	def GetExtentsSize(self):
		pass

	def GetModelCFrame(self):
		pass

	def GetModelSize(self):
		pass

	def GetPrimaryPartCFrame(self):
		pass

	def MakeJoints(self):
		pass

	def MoveTo(self, position: Vector3):
		pass

	def ResetOrientationToIdentity(self):
		pass

	def SetIdentityOrientation(self):
		pass

	def SetPrimaryPartCFrame(self, cframe: CFrame):
		pass

	def TranslateBy(self, delta: Vector3):
		pass

	def breakJoints(self):
		pass

	def makeJoints(self):
		pass

	def move(self, location: Vector3):
		pass

	def moveTo(self, location: Vector3):
		pass


	pass

class Actor:

	pass

class Status:

	pass

class WorldRoot:
	def ArePartsTouchingOthers(self, partList: Objects, overlapIgnored: float):
		pass

	def BulkMoveTo(self, partList: Objects, cframeList: list[Any], eventMode: BulkMoveMode):
		pass

	def FindPartOnRay(self, ray: Ray, ignoreDescendantsInstance: Instance, terrainCellsAreCubes: bool, ignoreWater: bool):
		pass

	def FindPartOnRayWithIgnoreList(self, ray: Ray, ignoreDescendantsTable: Objects, terrainCellsAreCubes: bool, ignoreWater: bool):
		pass

	def FindPartOnRayWithWhitelist(self, ray: Ray, whitelistDescendantsTable: Objects, ignoreWater: bool):
		pass

	def FindPartsInRegion3(self, region: Region3, ignoreDescendantsInstance: Instance, maxParts: int):
		pass

	def FindPartsInRegion3WithIgnoreList(self, region: Region3, ignoreDescendantsTable: Objects, maxParts: int):
		pass

	def FindPartsInRegion3WithWhiteList(self, region: Region3, whitelistDescendantsTable: Objects, maxParts: int):
		pass

	def GetPartBoundsInBox(self, cframe: CFrame, size: Vector3, overlapParams: OverlapParams):
		pass

	def GetPartBoundsInRadius(self, position: Vector3, radius: float, overlapParams: OverlapParams):
		pass

	def GetPartsInPart(self, part: BasePart, overlapParams: OverlapParams):
		pass

	def IKMoveTo(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float, collisionsMode: IKCollisionsMode):
		pass

	def IsRegion3Empty(self, region: Region3, ignoreDescendentsInstance: Instance):
		pass

	def IsRegion3EmptyWithIgnoreList(self, region: Region3, ignoreDescendentsTable: Objects):
		pass

	def Raycast(self, origin: Vector3, direction: Vector3, raycastParams: RaycastParams):
		pass

	def SetInsertPoint(self, point: Vector3, ignoreGrid: bool):
		pass

	def findPartOnRay(self, ray: Ray, ignoreDescendantsInstance: Instance, terrainCellsAreCubes: bool, ignoreWater: bool):
		pass

	def findPartsInRegion3(self, region: Region3, ignoreDescendantsInstance: Instance, maxParts: int):
		pass


	pass

class Workspace:
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
	def BreakJoints(self, objects: Objects):
		pass

	def CalculateJumpDistance(self, gravity: float, jumpPower: float, walkSpeed: float):
		pass

	def CalculateJumpHeight(self, gravity: float, jumpPower: float):
		pass

	def CalculateJumpPower(self, gravity: float, jumpHeight: float):
		pass

	def ExperimentalSolverIsEnabled(self):
		pass

	def GetNumAwakeParts(self):
		pass

	def GetPhysicsThrottling(self):
		pass

	def GetRealPhysicsFPS(self):
		pass

	def GetServerTimeNow(self):
		pass

	def JoinToOutsiders(self, objects: Objects, jointType: JointCreationMode):
		pass

	def MakeJoints(self, objects: Objects):
		pass

	def PGSIsEnabled(self):
		pass

	def SetMeshPartHeadsAndAccessories(self, value: MeshPartHeadsAndAccessories):
		pass

	def SetPhysicsThrottleEnabled(self, value: bool):
		pass

	def UnjoinFromOutsiders(self, objects: Objects):
		pass

	def ZoomToExtents(self):
		pass


	pass

class WorldModel:

	pass

class PackageLink:
	AutoUpdate: bool
	Creator: str
	PackageAssetName: str
	PackageId: Content
	PermissionLevel: PackagePermission
	Status: str
	VersionNumber: int

	pass

class PackageService:

	pass

class PackageUIService:
	def ConvertToPackageUpload(self, uploadUrl: str, cloneInstances: Objects, originalInstances: Objects):
		pass

	def GetPackageInfo(self, packageAssetId: int):
		pass

	def PublishPackage(self, packageInstance: Instance):
		pass

	def SetPackageVersion(self, packageInstance: Instance, versionNumber: int):
		pass


	pass

class Pages:
	IsFinished: bool
	def GetCurrentPage(self):
		pass

	def AdvanceToNextPageAsync(self):
		pass


	pass

class CatalogPages:

	pass

class DataStoreKeyPages:
	Cursor: str

	pass

class DataStoreListingPages:
	Cursor: str

	pass

class DataStorePages:

	pass

class DataStoreVersionPages:

	pass

class FriendPages:

	pass

class InventoryPages:

	pass

class EmotesPages:

	pass

class OutfitPages:

	pass

class StandardPages:

	pass

class PartOperationAsset:

	pass

class ParticleEmitter:
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
	def Clear(self):
		pass

	def Emit(self, particleCount: int):
		pass

	def FastForward(self, numFrames: int):
		pass


	pass

class Path:
	Status: PathStatus
	def GetPointCoordinates(self):
		pass

	def GetWaypoints(self):
		pass

	def CheckOcclusionAsync(self, start: int):
		pass

	def ComputeAsync(self, start: Vector3, finish: Vector3):
		pass


	pass

class PathfindingLink:
	Attachment0: Attachment
	Attachment1: Attachment
	IsBidirectional: bool
	Label: str

	pass

class PathfindingModifier:
	Label: str
	PassThrough: bool

	pass

class PathfindingService:
	EmptyCutoff: float
	def CreatePath(self, agentParameters: Dictionary):
		pass

	def ComputeRawPathAsync(self, start: Vector3, finish: Vector3, maxDistance: float):
		pass

	def ComputeSmoothPathAsync(self, start: Vector3, finish: Vector3, maxDistance: float):
		pass

	def FindPathAsync(self, start: Vector3, finish: Vector3):
		pass


	pass

class PausedState:
	AllThreadsPaused: bool
	Reason: DebuggerPauseReason
	ThreadId: int

	pass

class PausedStateBreakpoint:
	Breakpoint: Breakpoint

	pass

class PausedStateException:
	ExceptionText: str

	pass

class PermissionsService:
	def GetIsThirdPartyAssetAllowed(self):
		pass

	def GetIsThirdPartyPurchaseAllowed(self):
		pass

	def GetIsThirdPartyTeleportAllowed(self):
		pass

	def GetPermissions(self, assetId: str):
		pass

	def SetPermissions(self, assetId: str, permissions: list[Any]):
		pass


	pass

class PhysicsService:
	def CollisionGroupContainsPart(self, name: str, part: BasePart):
		pass

	def CollisionGroupSetCollidable(self, name1: str, name2: str, collidable: bool):
		pass

	def CollisionGroupsAreCollidable(self, name1: str, name2: str):
		pass

	def CreateCollisionGroup(self, name: str):
		pass

	def GetCollisionGroupId(self, name: str):
		pass

	def GetCollisionGroupName(self, name: int):
		pass

	def GetCollisionGroups(self):
		pass

	def GetMaxCollisionGroups(self):
		pass

	def GetRegisteredCollisionGroups(self):
		pass

	def IkSolve(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float):
		pass

	def IsCollisionGroupRegistered(self, name: str):
		pass

	def LocalIkSolve(self, part: BasePart, target: CFrame, translateStiffness: float, rotateStiffness: float):
		pass

	def RegisterCollisionGroup(self, name: str):
		pass

	def RemoveCollisionGroup(self, name: str):
		pass

	def RenameCollisionGroup(self, from: str, to: str):
		pass

	def SetPartCollisionGroup(self, part: BasePart, name: str):
		pass

	def UnregisterCollisionGroup(self, name: str):
		pass


	pass

class PhysicsSettings:
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

class Player:
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
	Team: Team
	def AddToBlockList(self, userIds: list[Any]):
		pass

	def ClearCharacterAppearance(self):
		pass

	def DistanceFromCharacter(self, point: Vector3):
		pass

	def GetFriendStatus(self, player: Self):
		pass

	def GetGameSessionID(self):
		pass

	def GetJoinData(self):
		pass

	def GetMouse(self):
		pass

	def GetNetworkPing(self):
		pass

	def GetUnder13(self):
		pass

	def HasAppearanceLoaded(self):
		pass

	def Kick(self, message: str):
		pass

	def LoadBoolean(self, key: str):
		pass

	def LoadCharacterAppearance(self, assetInstance: Instance):
		pass

	def LoadData(self):
		pass

	def LoadInstance(self, key: str):
		pass

	def LoadNumber(self, key: str):
		pass

	def LoadString(self, key: str):
		pass

	def Move(self, walkDirection: Vector3, relativeToCamera: bool):
		pass

	def RemoveCharacter(self):
		pass

	def RequestFriendship(self, player: Self):
		pass

	def RevokeFriendship(self, player: Self):
		pass

	def SaveBoolean(self, key: str, value: bool):
		pass

	def SaveData(self):
		pass

	def SaveInstance(self, key: str, value: Instance):
		pass

	def SaveNumber(self, key: str, value: float):
		pass

	def SaveString(self, key: str, value: str):
		pass

	def SetAccountAge(self, accountAge: int):
		pass

	def SetCharacterAppearanceJson(self, jsonBlob: str):
		pass

	def SetExperienceSettingsLocaleId(self, locale: str):
		pass

	def SetMembershipType(self, membershipType: MembershipType):
		pass

	def SetModerationAccessKey(self, moderationAccessKey: str):
		pass

	def SetSuperSafeChat(self, value: bool):
		pass

	def SetUnder13(self, value: bool):
		pass

	def UpdatePlayerBlocked(self, userId: int, blocked: bool):
		pass

	def loadBoolean(self, key: str):
		pass

	def loadInstance(self, key: str):
		pass

	def loadNumber(self, key: str):
		pass

	def loadString(self, key: str):
		pass

	def saveBoolean(self, key: str, value: bool):
		pass

	def saveInstance(self, key: str, value: Instance):
		pass

	def saveNumber(self, key: str, value: float):
		pass

	def saveString(self, key: str, value: str):
		pass

	def GetFriendsOnline(self, maxFriends: int):
		pass

	def GetRankInGroup(self, groupId: int):
		pass

	def GetRoleInGroup(self, groupId: int):
		pass

	def IsBestFriendsWith(self, userId: int):
		pass

	def IsFriendsWith(self, userId: int):
		pass

	def IsInGroup(self, groupId: int):
		pass

	def LoadCharacter(self):
		pass

	def LoadCharacterBlocking(self):
		pass

	def LoadCharacterWithHumanoidDescription(self, humanoidDescription: HumanoidDescription):
		pass

	def RequestStreamAroundAsync(self, position: Vector3, timeOut: float):
		pass

	def WaitForDataReady(self):
		pass

	def isFriendsWith(self, userId: int):
		pass

	def waitForDataReady(self):
		pass


	pass

class PlayerEmulatorService:
	CustomPoliciesEnabled: bool
	EmulatedCountryCode: str
	EmulatedGameLocale: str
	PlayerEmulationEnabled: bool
	SerializedEmulatedPolicyInfo: BinaryString
	def GetEmulatedPolicyInfo(self):
		pass

	def RegionCodeWillHaveAutomaticNonCustomPolicies(self, regionCode: str):
		pass

	def SetEmulatedPolicyInfo(self, emulatedPolicyInfo: Dictionary):
		pass


	pass

class PlayerScripts:
	def ClearComputerCameraMovementModes(self):
		pass

	def ClearComputerMovementModes(self):
		pass

	def ClearTouchCameraMovementModes(self):
		pass

	def ClearTouchMovementModes(self):
		pass

	def GetRegisteredComputerCameraMovementModes(self):
		pass

	def GetRegisteredComputerMovementModes(self):
		pass

	def GetRegisteredTouchCameraMovementModes(self):
		pass

	def GetRegisteredTouchMovementModes(self):
		pass

	def RegisterComputerCameraMovementMode(self, cameraMovementMode: ComputerCameraMovementMode):
		pass

	def RegisterComputerMovementMode(self, movementMode: ComputerMovementMode):
		pass

	def RegisterTouchCameraMovementMode(self, cameraMovementMode: TouchCameraMovementMode):
		pass

	def RegisterTouchMovementMode(self, movementMode: TouchMovementMode):
		pass


	pass

class Players:
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
	def Chat(self, message: str):
		pass

	def CreateLocalPlayer(self):
		pass

	def GetPlayerByUserId(self, userId: int):
		pass

	def GetPlayerFromCharacter(self, character: Model):
		pass

	def GetPlayers(self):
		pass

	def ReportAbuse(self, player: Player, reason: str, optionalMessage: str):
		pass

	def ReportAbuseV3(self, player: Player, jsonTags: str):
		pass

	def SetChatStyle(self, style: ChatStyle):
		pass

	def SetLocalPlayerInfo(self, userId: int, userName: str, displayName: str, membershipType: MembershipType, isUnder13: bool):
		pass

	def TeamChat(self, message: str):
		pass

	def WhisperChat(self, message: str, player: Instance):
		pass

	def getPlayers(self):
		pass

	def playerFromCharacter(self, character: Model):
		pass

	def players(self):
		pass

	def CreateHumanoidModelFromDescription(self, description: HumanoidDescription, rigType: HumanoidRigType, assetTypeVerification: AssetTypeVerification):
		pass

	def CreateHumanoidModelFromUserId(self, userId: int):
		pass

	def GetCharacterAppearanceAsync(self, userId: int):
		pass

	def GetCharacterAppearanceInfoAsync(self, userId: int):
		pass

	def GetFriendsAsync(self, userId: int):
		pass

	def GetHumanoidDescriptionFromOutfitId(self, outfitId: int):
		pass

	def GetHumanoidDescriptionFromUserId(self, userId: int):
		pass

	def GetNameFromUserIdAsync(self, userId: int):
		pass

	def GetUserIdFromNameAsync(self, userName: str):
		pass

	def GetUserThumbnailAsync(self, userId: int, thumbnailType: ThumbnailType, thumbnailSize: ThumbnailSize):
		pass


	pass

class Plugin:
	CollisionEnabled: bool
	GridSize: float
	HostDataModelType: StudioDataModelType
	HostDataModelTypeIsCurrent: bool
	UsesAssetInsertionDrag: bool
	MultipleDocumentInterfaceInstance: MultipleDocumentInterfaceInstance
	def Activate(self, exclusiveMouse: bool):
		pass

	def CreatePluginAction(self, actionId: str, text: str, statusTip: str, iconName: str, allowBinding: bool):
		pass

	def CreatePluginMenu(self, id: str, title: str, icon: str):
		pass

	def CreateToolbar(self, name: str):
		pass

	def Deactivate(self):
		pass

	def GetItem(self, key: str, defaultValue: Any):
		pass

	def GetJoinMode(self):
		pass

	def GetMouse(self):
		pass

	def GetSelectedRibbonTool(self):
		pass

	def GetSetting(self, key: str):
		pass

	def GetStudioUserId(self):
		pass

	def Invoke(self, key: str, arguments: tuple[Any]):
		pass

	def IsActivated(self):
		pass

	def IsActivatedWithExclusiveMouse(self):
		pass

	def Negate(self, objects: Objects):
		pass

	def OnInvoke(self, key: str, callback: Callable[..., Any]):
		pass

	def OnSetItem(self, key: str, callback: Callable[..., Any]):
		pass

	def OpenScript(self, script: LuaSourceContainer, lineNumber: int):
		pass

	def OpenWikiPage(self, url: str):
		pass

	def PauseSound(self, sound: Instance):
		pass

	def PlaySound(self, sound: Instance, normalizedTimePosition: float):
		pass

	def ResumeSound(self, sound: Instance):
		pass

	def SaveSelectedToRoblox(self):
		pass

	def SelectRibbonTool(self, tool: RibbonTool, position: UDim2):
		pass

	def Separate(self, objects: Objects):
		pass

	def SetItem(self, key: str, value: Any):
		pass

	def SetReady(self):
		pass

	def SetSetting(self, key: str, value: Any):
		pass

	def StartDecalDrag(self, decal: Instance):
		pass

	def StartDrag(self, dragData: Dictionary):
		pass

	def StopAllSounds(self):
		pass

	def Union(self, objects: Objects):
		pass

	def CreateDockWidgetPluginGui(self, pluginGuiId: str, dockWidgetPluginGuiInfo: DockWidgetPluginGuiInfo):
		pass

	def CreateQWidgetPluginGui(self, pluginGuiId: str, pluginGuiOptions: Dictionary):
		pass

	def ImportFbxAnimation(self, rigModel: Instance, isR15: bool):
		pass

	def ImportFbxRig(self, isR15: bool):
		pass

	def PromptForExistingAssetId(self, assetType: str):
		pass

	def PromptSaveSelection(self, suggestedFileName: str):
		pass


	pass

class PluginAction:
	ActionId: str
	AllowBinding: bool
	Checked: bool
	DefaultShortcut: str
	Enabled: bool
	StatusTip: str
	Text: str

	pass

class PluginDebugService:

	pass

class PluginDragEvent:
	Data: str
	MimeType: str
	Position: Vector2
	Sender: str

	pass

class PluginGuiService:

	pass

class PluginManagementService:
	def SetAutoUpdate(self, pluginId: int, state: bool):
		pass


	pass

class PluginManager:
	def CreatePlugin(self):
		pass

	def ExportPlace(self, filePath: str):
		pass

	def ExportSelection(self, filePath: str):
		pass


	pass

class PluginManagerInterface:
	def CreatePlugin(self):
		pass

	def ExportPlace(self, filePath: str):
		pass

	def ExportSelection(self, filePath: str):
		pass


	pass

class PluginMenu:
	Icon: str
	Title: str
	def AddAction(self, action: Instance):
		pass

	def AddMenu(self, menu: Instance):
		pass

	def AddNewAction(self, actionId: str, text: str, icon: str):
		pass

	def AddSeparator(self):
		pass

	def Clear(self):
		pass

	def ShowAsync(self):
		pass


	pass

class PluginPolicyService:
	def GetPluginPolicy(self, pluginName: str):
		pass


	pass

class PluginToolbar:
	def CreateButton(self, buttonId: str, tooltip: str, iconname: str, text: str):
		pass


	pass

class PluginToolbarButton:
	ClickableWhenViewportHidden: bool
	Enabled: bool
	Icon: Content
	def SetActive(self, active: bool):
		pass


	pass

class PointsService:
	def GetAwardablePoints(self):
		pass

	def AwardPoints(self, userId: int, amount: int):
		pass

	def GetGamePointBalance(self, userId: int):
		pass

	def GetPointBalance(self, userId: int):
		pass


	pass

class PolicyService:
	IsLuobuServer: TriStateBoolean
	LuobuWhitelisted: TriStateBoolean
	def GetPolicyInfoForPlayerAsync(self, player: Instance):
		pass

	def GetPolicyInfoForServerRobloxOnlyAsync(self):
		pass


	pass

class PoseBase:
	EasingDirection: PoseEasingDirection
	EasingStyle: PoseEasingStyle
	Weight: float

	pass

class NumberPose:
	Value: float

	pass

class Pose:
	MaskWeight: float
	CFrame: CFrame
	def AddSubPose(self, pose: Instance):
		pass

	def GetSubPoses(self):
		pass

	def RemoveSubPose(self, pose: Instance):
		pass


	pass

class PostEffect:
	Enabled: bool

	pass

class BloomEffect:
	Intensity: float
	Size: float
	Threshold: float

	pass

class BlurEffect:
	Size: float

	pass

class ColorCorrectionEffect:
	Brightness: float
	Contrast: float
	Saturation: float
	TintColor: Color3

	pass

class DepthOfFieldEffect:
	FarIntensity: float
	FocusDistance: float
	InFocusRadius: float
	NearIntensity: float

	pass

class SunRaysEffect:
	Intensity: float
	Spread: float

	pass

class ProcessInstancePhysicsService:

	pass

class ProximityPrompt:
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
	def InputHoldBegin(self):
		pass

	def InputHoldEnd(self):
		pass


	pass

class ProximityPromptService:
	Enabled: bool
	MaxPromptsVisible: int

	pass

class PublishService:
	def PublishDescendantAssets(self, instance: Instance):
		pass

	def PublishCageMeshAsync(self, wrap: Instance, cageType: CageType):
		pass


	pass

class RbxAnalyticsService:
	def AddGlobalPointsField(self, key: str, value: int):
		pass

	def AddGlobalPointsTag(self, key: str, value: str):
		pass

	def DEPRECATED_TrackEvent(self, category: str, action: str, label: str, value: int):
		pass

	def DEPRECATED_TrackEventWithArgs(self, category: str, action: str, label: str, args: Dictionary, value: int):
		pass

	def GetClientId(self):
		pass

	def GetSessionId(self):
		pass

	def ReleaseRBXEventStream(self, target: str):
		pass

	def RemoveGlobalPointsField(self, key: str):
		pass

	def RemoveGlobalPointsTag(self, key: str):
		pass

	def ReportCounter(self, counterName: str, amount: int):
		pass

	def ReportInfluxSeries(self, seriesName: str, points: Dictionary, throttlingPercentage: int):
		pass

	def ReportStats(self, category: str, value: float):
		pass

	def ReportToDiagByCountryCode(self, featureName: str, measureName: str, seconds: float):
		pass

	def SendEventDeferred(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SendEventImmediately(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SetRBXEvent(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def SetRBXEventStream(self, target: str, eventContext: str, eventName: str, additionalArgs: Dictionary):
		pass

	def TrackEvent(self, category: str, action: str, label: str, value: int):
		pass

	def TrackEventWithArgs(self, category: str, action: str, label: str, args: Dictionary, value: int):
		pass

	def UpdateHeartbeatObject(self, args: Dictionary):
		pass


	pass

class ReflectionMetadata:

	pass

class ReflectionMetadataCallbacks:

	pass

class ReflectionMetadataClasses:

	pass

class ReflectionMetadataEnums:

	pass

class ReflectionMetadataEvents:

	pass

class ReflectionMetadataFunctions:

	pass

class ReflectionMetadataItem:
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

class ReflectionMetadataClass:
	ExplorerImageIndex: int
	ExplorerOrder: int
	Insertable: bool
	PreferredParent: str

	pass

class ReflectionMetadataEnum:

	pass

class ReflectionMetadataEnumItem:

	pass

class ReflectionMetadataMember:

	pass

class ReflectionMetadataProperties:

	pass

class ReflectionMetadataYieldFunctions:

	pass

class RemoteDebuggerServer:

	pass

class RemoteEvent:
	def FireAllClients(self, arguments: tuple[Any]):
		pass

	def FireClient(self, player: Player, arguments: tuple[Any]):
		pass

	def FireServer(self, arguments: tuple[Any]):
		pass


	pass

class RemoteFunction:
	def InvokeClient(self, player: Player, arguments: tuple[Any]):
		pass

	def InvokeServer(self, arguments: tuple[Any]):
		pass


	pass

class RenderSettings:
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
	def GetMaxQualityLevel(self):
		pass


	pass

class RenderingTest:
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
	def RenderdocTriggerCapture(self):
		pass


	pass

class ReplicatedFirst:
	def IsDefaultLoadingGuiRemoved(self):
		pass

	def IsFinishedReplicating(self):
		pass

	def RemoveDefaultLoadingScreen(self):
		pass

	def SetDefaultLoadingGuiRemoved(self):
		pass


	pass

class ReplicatedStorage:

	pass

class RobloxPluginGuiService:

	pass

class RobloxReplicatedStorage:

	pass

class RotationCurve:
	Length: int
	def GetKeyAtIndex(self, index: int):
		pass

	def GetKeyIndicesAtTime(self, time: float):
		pass

	def GetKeys(self):
		pass

	def GetValueAtTime(self, time: float):
		pass

	def InsertKey(self, key: RotationCurveKey):
		pass

	def RemoveKeyAtIndex(self, startingIndex: int, count: int):
		pass

	def SetKeys(self, keys: list[Any]):
		pass


	pass

class RtMessagingService:

	pass

class RunService:
	ClientGitHash: str
	def BindToRenderStep(self, name: str, priority: int, function: Callable[..., Any]):
		pass

	def GetCoreScriptVersion(self):
		pass

	def GetRobloxClientChannel(self):
		pass

	def GetRobloxVersion(self):
		pass

	def IsClient(self):
		pass

	def IsEdit(self):
		pass

	def IsRunMode(self):
		pass

	def IsRunning(self):
		pass

	def IsServer(self):
		pass

	def IsStudio(self):
		pass

	def Pause(self):
		pass

	def Reset(self):
		pass

	def Run(self):
		pass

	def Set3dRenderingEnabled(self, enable: bool):
		pass

	def SetRobloxGuiFocused(self, focus: bool):
		pass

	def Stop(self):
		pass

	def UnbindFromRenderStep(self, name: str):
		pass

	def setThrottleFramerateEnabled(self, enable: bool):
		pass


	pass

class RuntimeScriptService:

	pass

class ScreenshotHud:
	CameraButtonIcon: Content
	CameraButtonPosition: UDim2
	CloseButtonPosition: UDim2
	CloseWhenScreenshotTaken: bool
	ExperienceNameOverlayEnabled: bool
	OverlayFont: Font
	UsernameOverlayEnabled: bool
	Visible: bool

	pass

class ScriptBuilder:

	pass

class CoreScriptBuilder:

	pass

class ScriptChangeService:

	pass

class ScriptCloneWatcher:

	pass

class ScriptCloneWatcherHelper:

	pass

class ScriptContext:
	ScriptsDisabled: bool
	def AddCoreScriptLocal(self, name: str, parent: Instance):
		pass

	def ClearScriptProfilingData(self):
		pass

	def DeserializeScriptProfilerString(self, jsonString: str):
		pass

	def GetCoverageStats(self):
		pass

	def SaveScriptProfilingData(self, filename: str):
		pass

	def SetTimeout(self, seconds: float):
		pass

	def StartScriptProfiling(self):
		pass

	def StopScriptProfiling(self):
		pass


	pass

class ScriptDebugger:
	CurrentLine: int
	IsDebugging: bool
	IsPaused: bool
	Script: Instance
	def AddWatch(self, expression: str):
		pass

	def GetBreakpoints(self):
		pass

	def GetGlobals(self, stackFrame: int):
		pass

	def GetLocals(self, stackFrame: int):
		pass

	def GetStack(self):
		pass

	def GetUpvalues(self, stackFrame: int):
		pass

	def GetWatchValue(self, watch: Instance):
		pass

	def GetWatches(self):
		pass

	def SetBreakpoint(self, line: int, isContextDependentBreakpoint: bool):
		pass

	def SetGlobal(self, name: str, value: Any, stackFrame: int):
		pass

	def SetLocal(self, name: str, value: Any, stackFrame: int):
		pass

	def SetUpvalue(self, name: str, value: Any, stackFrame: int):
		pass


	pass

class ScriptDocument:
	def GetInternalUri(self):
		pass

	def GetLine(self, lineIndex: int?):
		pass

	def GetLineCount(self):
		pass

	def GetScript(self):
		pass

	def GetSelectedText(self):
		pass

	def GetSelection(self):
		pass

	def GetSelectionEnd(self):
		pass

	def GetSelectionStart(self):
		pass

	def GetText(self, startLine: int?, startCharacter: int?, endLine: int?, endCharacter: int?):
		pass

	def GetViewport(self):
		pass

	def HasSelectedText(self):
		pass

	def IsCommandBar(self):
		pass

	def CloseAsync(self):
		pass

	def EditTextAsync(self, newText: str, startLine: int, startCharacter: int, endLine: int, endCharacter: int):
		pass

	def ForceSetSelectionAsync(self, cursorLine: int, cursorCharacter: int, anchorLine: int?, anchorCharacter: int?):
		pass

	def RequestSetSelectionAsync(self, cursorLine: int, cursorCharacter: int, anchorLine: int?, anchorCharacter: int?):
		pass


	pass

class ScriptEditorService:
	def DeregisterAutocompleteCallback(self, name: str):
		pass

	def FindScriptDocument(self, script: LuaSourceContainer):
		pass

	def GetScriptDocuments(self):
		pass

	def RegisterAutocompleteCallback(self, name: str, priority: int, callbackFunction: Callable[..., Any]):
		pass

	def OpenScriptDocumentAsync(self, script: LuaSourceContainer):
		pass


	pass

class ScriptRegistrationService:
	def GetSourceContainerByScriptGuid(self, guid: str):
		pass


	pass

class ScriptService:

	pass

class Selection:
	ActiveInstance: Instance
	SelectionLineThickness: int
	SelectionThickness: float
	def Add(self, instancesToAdd: Objects):
		pass

	def ClearTerrainSelectionHack(self):
		pass

	def Get(self):
		pass

	def Remove(self, instancesToRemove: Objects):
		pass

	def Set(self, selection: Objects):
		pass

	def SetTerrainSelectionHack(self, center: Vector3, size: Vector3):
		pass


	pass

class ServerScriptService:
	LoadStringEnabled: bool

	pass

class ServerStorage:

	pass

class ServiceProvider:
	def FindService(self, className: str):
		pass

	def GetService(self, className: str):
		pass

	def getService(self, className: str):
		pass

	def service(self, className: str):
		pass


	pass

class DataModel:
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
	def BindToClose(self, function: Callable[..., Any]):
		pass

	def DefineFastFlag(self, name: str, defaultValue: bool):
		pass

	def DefineFastInt(self, name: str, defaultValue: int):
		pass

	def DefineFastString(self, name: str, defaultValue: str):
		pass

	def GetEngineFeature(self, name: str):
		pass

	def GetFastFlag(self, name: str):
		pass

	def GetFastInt(self, name: str):
		pass

	def GetFastString(self, name: str):
		pass

	def GetJobsInfo(self):
		pass

	def GetMessage(self):
		pass

	def GetObjects(self, url: Content):
		pass

	def GetObjectsAllOrNone(self, url: Content):
		pass

	def GetObjectsList(self, urls: list[Any]):
		pass

	def GetRemoteBuildMode(self):
		pass

	def IsGearTypeAllowed(self, gearType: GearType):
		pass

	def IsLoaded(self):
		pass

	def Load(self, url: Content):
		pass

	def OpenScreenshotsFolder(self):
		pass

	def OpenVideosFolder(self):
		pass

	def ReportInGoogleAnalytics(self, category: str, action: str, label: str, value: int):
		pass

	def SetFastFlagForTesting(self, name: str, newValue: bool):
		pass

	def SetFastIntForTesting(self, name: str, newValue: int):
		pass

	def SetFastStringForTesting(self, name: str, newValue: str):
		pass

	def SetPlaceId(self, placeId: int):
		pass

	def SetUniverseId(self, universeId: int):
		pass

	def Shutdown(self):
		pass

	def GetObjectsAsync(self, url: Content):
		pass

	def HttpGetAsync(self, url: str, httpRequestType: HttpRequestType):
		pass

	def HttpPostAsync(self, url: str, data: str, contentType: str, httpRequestType: HttpRequestType):
		pass

	def InsertObjectsAndJoinIfLegacyAsync(self, url: Content):
		pass

	def SavePlace(self, saveFilter: SaveFilter):
		pass


	pass

class GenericSettings:

	pass

class AnalysticsSettings:

	pass

class GlobalSettings:
	def GetFFlag(self, name: str):
		pass

	def GetFVariable(self, name: str):
		pass


	pass

class UserSettings:
	def IsUserFeatureEnabled(self, name: str):
		pass

	def Reset(self):
		pass


	pass

class SessionService:
	def GetCreatedTimestampUtcMs(self, sid: str):
		pass

	def GetMetadata(self, sid: str, key: str):
		pass

	def GetRootSID(self):
		pass

	def RemoveMetadata(self, sid: str, key: str):
		pass

	def RemoveSession(self, sid: str):
		pass

	def RemoveSessionsWithMetadataKey(self, key: str):
		pass

	def ReplaceSession(self, sid: str, tag: str):
		pass

	def SessionExists(self, sid: str):
		pass

	def SetMetadata(self, sid: str, key: str, value: Any):
		pass

	def SetSession(self, parentSid: str, childSid: str, tag: str):
		pass


	pass

class Sky:
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

class Smoke:
	Color: Color3
	Enabled: bool
	Opacity: float
	RiseVelocity: float
	Size: float
	TimeScale: float
	def FastForward(self, numFrames: int):
		pass


	pass

class SnippetService:

	pass

class SocialService:
	def InvokeGameInvitePromptClosed(self, player: Instance, recipientIds: list[Any]):
		pass

	def PromptGameInvite(self, player: Instance):
		pass

	def CanSendGameInviteAsync(self, player: Instance, recipientId: int):
		pass


	pass

class Sound:
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
	SoundId: Content
	TimeLength: float
	TimePosition: float
	UsageContextPermission: UsageContext
	Volume: float
	isPlaying: bool
	RollOffMode: RollOffMode
	SoundGroup: SoundGroup
	def Pause(self):
		pass

	def Play(self):
		pass

	def Resume(self):
		pass

	def Stop(self):
		pass

	def pause(self):
		pass

	def play(self):
		pass

	def stop(self):
		pass


	pass

class SoundEffect:
	Enabled: bool
	Priority: int

	pass

class AssetSoundEffect:

	pass

class ChorusSoundEffect:
	Depth: float
	Mix: float
	Rate: float

	pass

class CompressorSoundEffect:
	Attack: float
	GainMakeup: float
	Ratio: float
	Release: float
	SideChain: Instance
	Threshold: float

	pass

class CustomSoundEffect:

	pass

class ChannelSelectorSoundEffect:
	Channel: int

	pass

class DistortionSoundEffect:
	Level: float

	pass

class EchoSoundEffect:
	Delay: float
	DryLevel: float
	Feedback: float
	WetLevel: float

	pass

class EqualizerSoundEffect:
	HighGain: float
	LowGain: float
	MidGain: float

	pass

class FlangeSoundEffect:
	Depth: float
	Mix: float
	Rate: float

	pass

class PitchShiftSoundEffect:
	Octave: float

	pass

class ReverbSoundEffect:
	DecayTime: float
	Density: float
	Diffusion: float
	DryLevel: float
	WetLevel: float

	pass

class TremoloSoundEffect:
	Depth: float
	Duty: float
	Frequency: float

	pass

class SoundGroup:
	Volume: float

	pass

class SoundService:
	AmbientReverb: ReverbType
	DistanceFactor: float
	DopplerScale: float
	RespectFilteringEnabled: bool
	RolloffScale: float
	VolumetricAudio: VolumetricAudio
	def BeginRecording(self):
		pass

	def GetListener(self):
		pass

	def GetOutputDevice(self):
		pass

	def GetOutputDevices(self):
		pass

	def GetSoundMemoryData(self):
		pass

	def PlayLocalSound(self, sound: Instance):
		pass

	def SetListener(self, listenerType: ListenerType, listener: tuple[Any]):
		pass

	def SetOutputDevice(self, name: str, guid: str):
		pass

	def SetRecordingDevice(self, deviceIndex: int):
		pass

	def EndRecording(self):
		pass

	def GetRecordingDevices(self):
		pass


	pass

class Sparkles:
	Color: Color3
	Enabled: bool
	SparkleColor: Color3
	TimeScale: float
	def FastForward(self, numFrames: int):
		pass


	pass

class SpawnerService:

	pass

class Speaker:
	ChannelCount: int
	PlaybackLoudness: float
	RollOffMaxDistance: float
	RollOffMinDistance: float
	Source: Instance
	Volume: float
	RollOffMode: RollOffMode
	SoundGroup: SoundGroup

	pass

class StackFrame:
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

class StandalonePluginScripts:

	pass

class StarterGear:

	pass

class StarterPack:

	pass

class StarterPlayer:
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
	def ClearDefaults(self):
		pass


	pass

class StarterPlayerScripts:

	pass

class StarterCharacterScripts:

	pass

class Stats:
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
	def GetBrowserTrackerId(self):
		pass

	def GetMemoryUsageMbForTag(self, tag: DeveloperMemoryTag):
		pass

	def GetTotalMemoryUsageMb(self):
		pass

	def GetPaginatedMemoryByTexture(self, queryType: TextureQueryType, pageIndex: int, pageSize: int):
		pass


	pass

class StatsItem:
	DisplayName: str
	def GetValue(self):
		pass

	def GetValueString(self):
		pass


	pass

class RunningAverageItemDouble:

	pass

class RunningAverageItemInt:

	pass

class RunningAverageTimeIntervalItem:

	pass

class TotalCountTimeIntervalItem:

	pass

class StopWatchReporter:
	def FinishTask(self, taskId: int):
		pass

	def SendReport(self, reportName: str):
		pass

	def StartTask(self, reportName: str, taskName: str):
		pass


	pass

class Studio:
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
	def GetAvailableThemes(self):
		pass


	pass

class StudioAssetService:
	def ConvertToPackageUpload(self, uploadUrl: str, cloneInstances: Objects, originalInstances: Objects):
		pass

	def SerializeInstances(self, instances: Objects):
		pass


	pass

class StudioData:
	EnableScriptCollabByDefaultOnLoad: bool
	SrcPlaceId: int
	SrcUniverseId: int

	pass

class StudioDeviceEmulatorService:
	HasMultiTouchStarted: bool
	IsMultiTouchEmulationOn: bool
	IsMultiTouchEnabled: bool
	PivotPosition: Vector2
	def GetMaxNumTouches(self):
		pass

	def GetTouchInBounds(self, index: int):
		pass

	def GetTouchPosition(self, index: int):
		pass

	def EmulatePCDeviceWithResolution(self, deviceId: str, resolution: Vector2):
		pass

	def GetCurrentDeviceId(self):
		pass

	def GetCurrentOrientation(self):
		pass

	def HasDeviceWithId(self, deviceId: str):
		pass

	def SetCurrentDeviceId(self, deviceId: str):
		pass

	def SetCurrentOrientation(self, orientation: ScreenOrientation):
		pass


	pass

class StudioHighDpiService:
	def IsNotHighDPIAwareBuild(self):
		pass


	pass

class StudioPublishService:
	def ClearUploadNames(self):
		pass

	def PublishAs(self, universeId: int, placeId: int, groupId: int, isPublish: bool, publishParameters: Any):
		pass

	def PublishThenTurnOnTeamCreate(self):
		pass

	def RefreshDocumentDisplayName(self):
		pass

	def SetTeamCreateOnPublishInfo(self, shouldTurnOnTcOnPublish: bool, newPlaceName: str):
		pass

	def SetUniverseDisplayName(self, newName: str):
		pass

	def SetUploadNames(self, placeName: str, universeName: str):
		pass

	def ShowSaveOrPublishPlaceToRoblox(self, showGameSelect: bool, isPublish: bool, closeMode: StudioCloseMode):
		pass


	pass

class StudioScriptDebugEventListener:

	pass

class StudioService:
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
	def AnimationIdSelected(self, id: int):
		pass

	def CopyToClipboard(self, stringToCopy: str):
		pass

	def GetBadgeConfigureUrl(self, badgeId: int):
		pass

	def GetBadgeUploadUrl(self):
		pass

	def GetClassIcon(self, className: str):
		pass

	def GetPlaceIsPersistedToCloud(self):
		pass

	def GetResourceByCategory(self, category: str):
		pass

	def GetStartupAssetId(self):
		pass

	def GetStartupPluginId(self):
		pass

	def GetTermsOfUseUrl(self):
		pass

	def GetUserId(self):
		pass

	def GizmoRaycast(self, origin: Vector3, direction: Vector3, raycastParams: RaycastParams):
		pass

	def HasInternalPermission(self):
		pass

	def IsPluginInstalled(self, assetId: int):
		pass

	def IsPluginUpToDate(self, assetId: int, currentAssetVersion: int):
		pass

	def OpenInBrowser_DONOTUSE(self, url: str):
		pass

	def RequestClose(self, closeMode: StudioCloseMode):
		pass

	def SetPluginEnabled(self, assetId: int, state: bool):
		pass

	def ShowPlaceVersionHistoryDialog(self, placeId: int):
		pass

	def ShowPublishToRoblox(self):
		pass

	def UninstallPlugin(self, assetId: int):
		pass

	def UpdatePluginManagement(self):
		pass

	def PromptImportFile(self, fileTypeFilter: list[Any]):
		pass

	def PromptImportFiles(self, fileTypeFilter: list[Any]):
		pass

	def TryInstallPlugin(self, assetId: int, assetVersionId: int):
		pass


	pass

class StudioTheme:
	def GetColor(self, styleguideitem: StudioStyleGuideColor, modifier: StudioStyleGuideModifier):
		pass


	pass

class SurfaceAppearance:
	ColorMap: Content
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	TexturePack: Content
	AlphaMode: AlphaMode

	pass

class TaskScheduler:
	SchedulerDutyCycle: float
	SchedulerRate: float
	ThreadPoolSize: int
	ThreadPoolConfig: ThreadPoolConfig

	pass

class Team:
	AutoAssignable: bool
	AutoColorCharacters: bool
	ChildOrder: int
	Score: int
	TeamColor: BrickColor
	def GetPlayers(self):
		pass


	pass

class TeamCreateService:
	def SendUnarchiveUniverseAsync(self, universeId: int):
		pass


	pass

class Teams:
	def GetTeams(self):
		pass

	def RebalanceTeams(self):
		pass


	pass

class TeleportAsyncResult:
	PrivateServerId: str
	ReservedServerAccessCode: str

	pass

class TeleportOptions:
	ReservedServerAccessCode: str
	ServerInstanceId: str
	ShouldReserveServer: bool
	def GetTeleportData(self):
		pass

	def SetTeleportData(self, teleportData: Any):
		pass


	pass

class TeleportService:
	CustomizedTeleportUI: bool
	def Block(self):
		pass

	def GetArrivingTeleportGui(self):
		pass

	def GetLocalPlayerTeleportData(self):
		pass

	def GetTeleportSetting(self, setting: str):
		pass

	def SetTeleportGui(self, gui: Instance):
		pass

	def SetTeleportSetting(self, setting: str, value: Any):
		pass

	def Teleport(self, placeId: int, player: Instance, teleportData: Any, customLoadingScreen: Instance):
		pass

	def TeleportCancel(self):
		pass

	def TeleportToPlaceInstance(self, placeId: int, instanceId: str, player: Instance, spawnName: str, teleportData: Any, customLoadingScreen: Instance):
		pass

	def TeleportToPrivateServer(self, placeId: int, reservedServerAccessCode: str, players: Objects, spawnName: str, teleportData: Any, customLoadingScreen: Instance):
		pass

	def TeleportToSpawnByName(self, placeId: int, spawnName: str, player: Instance, teleportData: Any, customLoadingScreen: Instance):
		pass

	def GetPlayerPlaceInstanceAsync(self, userId: int):
		pass

	def ReserveServer(self, placeId: int):
		pass

	def TeleportAsync(self, placeId: int, players: Objects, teleportOptions: Instance):
		pass

	def TeleportPartyAsync(self, placeId: int, players: Objects, teleportData: Any, customLoadingScreen: Instance):
		pass

	def UnblockAsync(self):
		pass


	pass

class TemporaryCageMeshProvider:

	pass

class TemporaryScriptService:

	pass

class TerrainDetail:
	ColorMap: Content
	Face: TerrainFace
	MetalnessMap: Content
	NormalMap: Content
	RoughnessMap: Content
	StudsPerTile: float
	MaterialPattern: MaterialPattern

	pass

class TerrainRegion:
	IsSmooth: bool
	SizeInCells: Vector3
	def ConvertToSmooth(self):
		pass


	pass

class TestService:
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
	def Check(self, condition: bool, description: str, source: Instance, line: int):
		pass

	def Checkpoint(self, text: str, source: Instance, line: int):
		pass

	def Done(self):
		pass

	def Error(self, description: str, source: Instance, line: int):
		pass

	def Fail(self, description: str, source: Instance, line: int):
		pass

	def Message(self, text: str, source: Instance, line: int):
		pass

	def Require(self, condition: bool, description: str, source: Instance, line: int):
		pass

	def ScopeTime(self):
		pass

	def Warn(self, condition: bool, description: str, source: Instance, line: int):
		pass

	def isFeatureEnabled(self, name: str):
		pass

	def Run(self):
		pass


	pass

class TextBoxService:

	pass

class TextChannel:
	def DisplaySystemMessage(self, systemMessage: str, metadata: str):
		pass

	def AddUserAsync(self, userId: int):
		pass

	def SendAsync(self, message: str, metadata: str):
		pass


	pass

class TextChatCommand:
	Enabled: bool
	PrimaryAlias: str
	SecondaryAlias: str

	pass

class TextChatConfigurations:

	pass

class BubbleChatConfiguration:
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

class ChatInputBarConfiguration:
	AbsolutePosition: Vector2
	AbsolutePositionWrite: Vector2
	AbsoluteSize: Vector2
	AbsoluteSizeWrite: Vector2
	Enabled: bool
	TargetTextChannel: TextChannel

	pass

class ChatWindowConfiguration:
	AbsolutePosition: Vector2
	AbsolutePositionWrite: Vector2
	AbsoluteSize: Vector2
	AbsoluteSizeWrite: Vector2
	Enabled: bool
	HorizontalAlignment: HorizontalAlignment
	VerticalAlignment: VerticalAlignment

	pass

class TextChatMessage:
	MessageId: str
	Metadata: str
	PrefixText: str
	Status: TextChatMessageStatus
	Text: str
	Timestamp: DateTime
	TextChannel: TextChannel
	TextSource: TextSource

	pass

class TextChatMessageProperties:
	PrefixText: str
	Text: str

	pass

class TextChatService:
	CreateDefaultCommands: bool
	CreateDefaultTextChannels: bool
	ChatVersion: ChatVersion

	pass

class TextFilterResult:
	def GetChatForUserAsync(self, toUserId: int):
		pass

	def GetNonChatStringForBroadcastAsync(self):
		pass

	def GetNonChatStringForUserAsync(self, toUserId: int):
		pass


	pass

class TextService:
	def GetTextSize(self, string: str, fontSize: int, font: Font, frameSize: Vector2):
		pass

	def SetResolutionScale(self, scale: float):
		pass

	def FilterStringAsync(self, stringToFilter: str, fromUserId: int, textContext: TextFilterContext):
		pass

	def GetFamilyInfoAsync(self, assetId: Content):
		pass

	def GetTextBoundsAsync(self, params: GetTextBoundsParams):
		pass


	pass

class TextSource:
	CanSend: bool
	UserId: int

	pass

class ThirdPartyUserService:
	def GetUserPlatformId(self):
		pass

	def GetUserPlatformName(self):
		pass

	def HaveActiveUser(self):
		pass

	def ReturnToEngagement(self):
		pass

	def ShowAccountPicker(self):
		pass

	def RegisterActiveUser(self, gamepadId: UserInputType):
		pass


	pass

class ThreadState:
	FrameCount: int
	Populated: bool
	ThreadId: int
	ThreadName: str
	def GetFrame(self, index: int):
		pass


	pass

class TimerService:

	pass

class ToastNotificationService:
	def HideNotification(self, notificationId: str):
		pass

	def ShowNotification(self, message: str, notificationId: str):
		pass


	pass

class TouchInputService:

	pass

class TouchTransmitter:

	pass

class TracerService:
	def FinishSpan(self, spanId: str):
		pass

	def StartSpan(self, name: str, parentId: str):
		pass


	pass

class TrackerLodController:
	AudioMode: TrackerLodFlagMode
	VideoExtrapolationMode: TrackerExtrapolationFlagMode
	VideoLodMode: TrackerLodValueMode
	VideoMode: TrackerLodFlagMode
	def getExtrapolation(self):
		pass

	def getVideoLod(self):
		pass

	def isAudioEnabled(self):
		pass

	def isVideoEnabled(self):
		pass


	pass

class TrackerStreamAnimation:

	pass

class Trail:
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
	def Clear(self):
		pass


	pass

class Translator:
	LocaleId: str
	def FormatByKey(self, key: str, args: Any):
		pass

	def RobloxOnlyTranslate(self, context: Instance, text: str):
		pass

	def Translate(self, context: Instance, text: str):
		pass


	pass

class TweenBase:
	PlaybackState: PlaybackState
	def Cancel(self):
		pass

	def Pause(self):
		pass

	def Play(self):
		pass


	pass

class Tween:
	Instance: Instance
	TweenInfo: TweenInfo

	pass

class TweenService:
	def Create(self, instance: Instance, tweenInfo: TweenInfo, propertyTable: Dictionary):
		pass

	def GetValue(self, alpha: float, easingStyle: EasingStyle, easingDirection: EasingDirection):
		pass


	pass

class UGCValidationService:
	def GetMeshTriCountSync(self, meshId: str):
		pass

	def GetMeshVertsSync(self, meshId: str):
		pass

	def GetTextureSizeSync(self, textureId: str):
		pass

	def ResetCollisionFidelity(self, meshPart: Instance):
		pass

	def SetMeshIdBlocking(self, meshPart: Instance, meshId: str):
		pass

	def FetchAssetWithFormat(self, url: Content, assetFormat: str):
		pass

	def GetMeshTriCount(self, meshId: str):
		pass

	def GetMeshVertColors(self, meshId: str):
		pass

	def GetMeshVerts(self, meshId: str):
		pass

	def GetTextureSize(self, textureId: str):
		pass

	def ValidateCageMeshIntersection(self, innerCageMeshId: str, outerCageMeshId: str, refMeshId: str):
		pass

	def ValidateCageNonManifoldAndHoles(self, meshId: str):
		pass

	def ValidateFullBodyCageDeletion(self, meshId: str):
		pass

	def ValidateMeshTriangles(self, meshId: str):
		pass

	def ValidateMeshVertColors(self, meshId: str):
		pass

	def ValidateMisMatchUV(self, innerCageMeshId: str, outerCageMeshId: str):
		pass

	def ValidateOverlappingVertices(self, meshId: str):
		pass

	def ValidateTextureSize(self, textureId: str):
		pass

	def ValidateUVSpace(self, meshId: str):
		pass


	pass

class UIBase:

	pass

class UIComponent:

	pass

class UIConstraint:

	pass

class UIAspectRatioConstraint:
	AspectRatio: float
	AspectType: AspectType
	DominantAxis: DominantAxis

	pass

class UISizeConstraint:
	MaxSize: Vector2
	MinSize: Vector2

	pass

class UITextSizeConstraint:
	MaxTextSize: int
	MinTextSize: int

	pass

class UICorner:
	CornerRadius: UDim

	pass

class UIGradient:
	Color: ColorSequence
	Enabled: bool
	Offset: Vector2
	Rotation: float
	Transparency: NumberSequence

	pass

class UILayout:

	pass

class UIGridStyleLayout:
	AbsoluteContentSize: Vector2
	FillDirection: FillDirection
	HorizontalAlignment: HorizontalAlignment
	SortOrder: SortOrder
	VerticalAlignment: VerticalAlignment
	def ApplyLayout(self):
		pass

	def SetCustomSortFunction(self, function: Callable[..., Any]):
		pass


	pass

class UIGridLayout:
	AbsoluteCellCount: Vector2
	AbsoluteCellSize: Vector2
	CellPadding: UDim2
	CellSize: UDim2
	FillDirectionMaxCells: int
	StartCorner: StartCorner

	pass

class UIListLayout:
	Padding: UDim

	pass

class UIPageLayout:
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
	def JumpTo(self, page: Instance):
		pass

	def JumpToIndex(self, index: int):
		pass

	def Next(self):
		pass

	def Previous(self):
		pass


	pass

class UITableLayout:
	FillEmptySpaceColumns: bool
	FillEmptySpaceRows: bool
	MajorAxis: TableMajorAxis
	Padding: UDim2

	pass

class UIPadding:
	PaddingBottom: UDim
	PaddingLeft: UDim
	PaddingRight: UDim
	PaddingTop: UDim

	pass

class UIScale:
	Scale: float

	pass

class UIStroke:
	Color: Color3
	Enabled: bool
	Thickness: float
	Transparency: float
	ApplyStrokeMode: ApplyStrokeMode
	LineJoinMode: LineJoinMode

	pass

class UnvalidatedAssetService:
	def AppendTempAssetId(self, userId: int, id: int, lookAt: Vector3, camPos: Vector3, usage: str):
		pass

	def AppendVantagePoint(self, userId: int, id: int, lookAt: Vector3, camPos: Vector3):
		pass

	def UpgradeTempAssetId(self, userId: int, tempId: int, assetId: int):
		pass


	pass

class UserGameSettings:
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
	def GetCameraYInvertValue(self):
		pass

	def GetOnboardingCompleted(self, onboardingId: str):
		pass

	def GetTutorialState(self, tutorialId: str):
		pass

	def InFullScreen(self):
		pass

	def InStudioMode(self):
		pass

	def ResetOnboardingCompleted(self, onboardingId: str):
		pass

	def SetCameraYInvertVisible(self):
		pass

	def SetGamepadCameraSensitivityVisible(self):
		pass

	def SetOnboardingCompleted(self, onboardingId: str):
		pass

	def SetTutorialState(self, tutorialId: str, value: bool):
		pass


	pass

class UserInputService:
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
	def GamepadSupports(self, gamepadNum: UserInputType, gamepadKeyCode: KeyCode):
		pass

	def GetConnectedGamepads(self):
		pass

	def GetDeviceAcceleration(self):
		pass

	def GetDeviceGravity(self):
		pass

	def GetDeviceRotation(self):
		pass

	def GetDeviceType(self):
		pass

	def GetFocusedTextBox(self):
		pass

	def GetGamepadConnected(self, gamepadNum: UserInputType):
		pass

	def GetGamepadState(self, gamepadNum: UserInputType):
		pass

	def GetKeysPressed(self):
		pass

	def GetLastInputType(self):
		pass

	def GetMouseButtonsPressed(self):
		pass

	def GetMouseDelta(self):
		pass

	def GetMouseLocation(self):
		pass

	def GetNavigationGamepads(self):
		pass

	def GetPlatform(self):
		pass

	def GetStringForKeyCode(self, keyCode: KeyCode):
		pass

	def GetSupportedGamepadKeyCodes(self, gamepadNum: UserInputType):
		pass

	def GetUserCFrame(self, type: UserCFrame):
		pass

	def IsGamepadButtonDown(self, gamepadNum: UserInputType, gamepadKeyCode: KeyCode):
		pass

	def IsKeyDown(self, keyCode: KeyCode):
		pass

	def IsMouseButtonPressed(self, mouseButton: UserInputType):
		pass

	def IsNavigationGamepad(self, gamepadEnum: UserInputType):
		pass

	def RecenterUserHeadCFrame(self):
		pass

	def SendAppUISizes(self, statusBarSize: Vector2, navBarSize: Vector2, bottomBarSize: Vector2, rightBarSize: Vector2):
		pass

	def SetNavigationGamepad(self, gamepadEnum: UserInputType, enabled: bool):
		pass


	pass

class UserService:
	def GetUserInfosByUserIdsAsync(self, userIds: list[Any]):
		pass


	pass

class VRService:
	DidPointerHit: bool
	GuiInputUserCFrame: UserCFrame
	LaserDistance: float
	PointerHitCFrame: CFrame
	VRDeviceAvailable: bool
	VRDeviceName: str
	VREnabled: bool
	def GetTouchpadMode(self, pad: VRTouchpad):
		pass

	def GetUserCFrame(self, type: UserCFrame):
		pass

	def GetUserCFrameEnabled(self, type: UserCFrame):
		pass

	def IsMaquettes(self):
		pass

	def IsVRAppBuild(self):
		pass

	def RecenterUserHeadCFrame(self):
		pass

	def RequestNavigation(self, cframe: CFrame, inputUserCFrame: UserCFrame):
		pass

	def SetTouchpadMode(self, pad: VRTouchpad, mode: VRTouchpadMode):
		pass


	pass

class ValueBase:

	pass

class BinaryStringValue:

	pass

class BoolValue:
	Value: bool

	pass

class BrickColorValue:
	Value: BrickColor

	pass

class CFrameValue:
	Value: CFrame

	pass

class Color3Value:
	Value: Color3

	pass

class DoubleConstrainedValue:
	ConstrainedValue: float
	MaxValue: float
	MinValue: float
	Value: float

	pass

class IntConstrainedValue:
	ConstrainedValue: int
	MaxValue: int
	MinValue: int
	Value: int

	pass

class IntValue:
	Value: int

	pass

class NumberValue:
	Value: float

	pass

class ObjectValue:
	Value: Instance

	pass

class RayValue:
	Value: Ray

	pass

class StringValue:
	Value: str

	pass

class Vector3Value:
	Value: Vector3

	pass

class Vector3Curve:
	def GetValueAtTime(self, time: float):
		pass

	def X(self):
		pass

	def Y(self):
		pass

	def Z(self):
		pass


	pass

class VersionControlService:
	ScriptCollabEnabled: bool

	pass

class VideoCaptureService:
	Active: bool
	CameraID: str
	def GetCameraDevices(self):
		pass


	pass

class VirtualInputManager:
	AdditionalLuaState: str
	def Dump(self):
		pass

	def HandleGamepadAxisInput(self, objectId: int, keyCode: KeyCode, x: float, y: float, z: float):
		pass

	def HandleGamepadButtonInput(self, deviceId: int, keyCode: KeyCode, buttonState: int):
		pass

	def HandleGamepadConnect(self, deviceId: int):
		pass

	def HandleGamepadDisconnect(self, deviceId: int):
		pass

	def SendAccelerometerEvent(self, x: float, y: float, z: float):
		pass

	def SendGravityEvent(self, x: float, y: float, z: float):
		pass

	def SendGyroscopeEvent(self, quatX: float, quatY: float, quatZ: float, quatW: float):
		pass

	def SendKeyEvent(self, isPressed: bool, keyCode: KeyCode, isRepeatedKey: bool, layerCollector: Instance):
		pass

	def SendMouseButtonEvent(self, x: int, y: int, mouseButton: int, isDown: bool, layerCollector: Instance, repeatCount: int):
		pass

	def SendMouseMoveEvent(self, x: float, y: float, layerCollector: Instance):
		pass

	def SendMouseWheelEvent(self, x: float, y: float, isForwardScroll: bool, layerCollector: Instance):
		pass

	def SendTextInputCharacterEvent(self, str: str, layerCollector: Instance):
		pass

	def SendTouchEvent(self, touchId: int, state: int, x: float, y: float):
		pass

	def SetInputTypesToIgnore(self, inputTypesToIgnore: Any):
		pass

	def StartPlaying(self, fileName: str):
		pass

	def StartPlayingJSON(self, string: str):
		pass

	def StartRecording(self):
		pass

	def StopPlaying(self):
		pass

	def StopRecording(self):
		pass

	def sendRobloxEvent(self, namespace: str, detail: str, detailType: str):
		pass

	def sendThemeChangeEvent(self, themeName: str):
		pass

	def WaitForInputEventsProcessed(self):
		pass


	pass

class VirtualUser:
	def Button1Down(self, position: Vector2, camera: CFrame):
		pass

	def Button1Up(self, position: Vector2, camera: CFrame):
		pass

	def Button2Down(self, position: Vector2, camera: CFrame):
		pass

	def Button2Up(self, position: Vector2, camera: CFrame):
		pass

	def CaptureController(self):
		pass

	def ClickButton1(self, position: Vector2, camera: CFrame):
		pass

	def ClickButton2(self, position: Vector2, camera: CFrame):
		pass

	def MoveMouse(self, position: Vector2, camera: CFrame):
		pass

	def SetKeyDown(self, key: str):
		pass

	def SetKeyUp(self, key: str):
		pass

	def StartRecording(self):
		pass

	def StopRecording(self):
		pass

	def TypeKey(self, key: str):
		pass


	pass

class VisibilityService:

	pass

class Visit:

	pass

class VoiceChannel:
	def AddUserAsync(self, userId: int):
		pass


	pass

class VoiceChatInternal:
	VoiceChatState: VoiceChatState
	def GetAndClearCallFailureMessage(self):
		pass

	def GetAudioProcessingSettings(self):
		pass

	def GetChannelId(self):
		pass

	def GetGroupId(self):
		pass

	def GetMicDevices(self):
		pass

	def GetParticipants(self):
		pass

	def GetSpeakerDevices(self):
		pass

	def GetVoiceChatApiVersion(self):
		pass

	def GetVoiceChatAvailable(self):
		pass

	def IsContextVoiceEnabled(self):
		pass

	def IsPublishPaused(self):
		pass

	def IsSubscribePaused(self, userId: int):
		pass

	def JoinByGroupId(self, groupId: str, isMicMuted: bool):
		pass

	def JoinByGroupIdToken(self, groupId: str, isMicMuted: bool):
		pass

	def Leave(self):
		pass

	def PublishPause(self, paused: bool):
		pass

	def SetMicDevice(self, micDeviceName: str, micDeviceGuid: str):
		pass

	def SetSpeakerDevice(self, speakerDeviceName: str, speakerDeviceGuid: str):
		pass

	def SubscribeBlock(self, userId: int):
		pass

	def SubscribePause(self, userId: int, paused: bool):
		pass

	def SubscribePauseAll(self, paused: bool):
		pass

	def SubscribeRetry(self, userId: int):
		pass

	def SubscribeUnblock(self, userId: int):
		pass

	def IsVoiceEnabledForUserIdAsync(self, userId: int):
		pass


	pass

class VoiceChatService:
	EnableDefaultVoice: bool
	VoiceChatEnabledForPlaceOnRcc: bool
	VoiceChatEnabledForUniverseOnRcc: bool
	def IsVoiceEnabledForUserIdAsync(self, userId: int):
		pass


	pass

class VoiceSource:
	UserId: int

	pass

class WeldConstraint:
	Active: bool
	Enabled: bool
	Part0: BasePart
	Part1: BasePart

	pass

