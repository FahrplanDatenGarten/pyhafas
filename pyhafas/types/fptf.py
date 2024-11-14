import datetime
from enum import Enum
from typing import List, Optional


class Mode(Enum):
    """
    FPTF `Mode` object

    The mode of a `Leg` specifies the general type of transport vehicle (it can also be a walking leg)
    """
    TRAIN = 'train'
    BUS = 'bus'
    WATERCRAFT = 'watercraft'
    TAXI = 'taxi'
    GONDOLA = 'gondola'
    AIRCRAFT = 'aircraft'
    CAR = 'car'
    BICYCLE = 'bicycle'
    WALKING = 'walking'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class FPTFObject:
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Station(FPTFObject):
    """
    FPTF `Station` object

    A station is a point where vehicles stop. It may be a larger building or just a small stop without special infrastructure.

    :ivar id: ID of the Station. Typically a number but as a string
    :vartype id: str
    :ivar lid: Location ID of the Station (maybe `None`). Long-form, containing multiple fields
    :vartype lid: Optional[str]
    :ivar name: Name of the Station (maybe `None`)
    :vartype name: Optional[str]
    :ivar latitude: Latitude coordinate of the Station (maybe `None`)
    :vartype latitude: Optional[float]
    :ivar longitude: Longitude coordinate of the Station (maybe `None`)
    :vartype longitude: Optional[float]
    """

    def __init__(
            self,
            id: str,
            lid: Optional[str] = None,
            name: Optional[str] = None,
            latitude: Optional[float] = None,
            longitude: Optional[float] = None):
        """
        FPTF `Station` object

        :param id: Internal ID of the station
        :param lid: (optional) Internal Location ID of the station. Defaults to None
        :param name: (optional) Name of the station. Defaults to None
        :param latitude: (optional) Latitude coordinate of the station. Defaults to None
        :param longitude: (optional) Longitude coordinate of the station. Defaults to None
        """
        self.id: str = id
        self.lid: Optional[str] = lid
        self.name: Optional[str] = name
        self.latitude: Optional[float] = latitude
        self.longitude: Optional[float] = longitude


class Remark(FPTFObject):
    """
    A remark is a textual comment/information, usually added to a Stopover or Leg

    :ivar remark_type: Type/Category of the remark. May have a different meaning depending on the network
    :vartype remark_type: Optional[str]
    :ivar code: Code of the remark. May have a different meaning depending on the network
    :vartype code: Optional[str]
    :ivar subject: Subject of the remark
    :vartype subject: Optional[str]
    :ivar text: Actual content of the remark
    :vartype text: Optional[str]
    :ivar priority: Priority of the remark, higher is better
    :vartype priority: Optional[int]
    :ivar trip_id: ID to a Trip added to this remark (e.g. a replacement train)
    :vartype trip_id: Optional[str]
    """
    def __init__(
            self,
            remark_type: Optional[str] = None,
            code: Optional[str] = None,
            subject: Optional[str] = None,
            text: Optional[str] = None,
            priority: Optional[int] = None,
            trip_id: Optional[str] = None):
        """

        :param remark_type: Type/Category of the remark. May have a different meaning depending on the network
        :param code: Code of the remark. May have a different meaning depending on the network
        :param subject: Subject of the remark
        :param text: Actual content of the remark
        :param priority: Priority of the remark, higher is better
        :param trip_id: ID to a Trip added to this remark (e.g. a replacement train)
        """
        self.remark_type: Optional[str] = remark_type
        self.code: Optional[str] = code
        self.subject: Optional[str] = subject
        self.text: Optional[str] = text
        self.priority: Optional[int] = priority
        self.trip_id: Optional[str] = trip_id


class Stopover(FPTFObject):
    """
    FPTF `Stopover` object

    A stopover represents a vehicle stopping at a stop/station at a specific time.

    :ivar stop: Station where the vehicle is stopping
    :vartype stop: Station
    :ivar cancelled: Whether the stop is cancelled
    :vartype cancelled: bool
    :ivar arrival: Planned arrival date and time at the station (maybe `None`)
    :vartype arrival: Optional[datetime.datetime]
    :ivar arrivalDelay: Arrival delay at the station (maybe `None`)
    :vartype arrivalDelay: Optional[datetime.timedelta]
    :ivar arrivalPlatform: Real-time arrival platform at the station (maybe `None`)
    :vartype arrivalPlatform: Optional[str]
    :ivar departure: Planned departure date and time at the station (maybe `None`)
    :vartype departure: Optional[datetime.datetime]
    :ivar departureDelay: Departure delay at the station (maybe `None`)
    :vartype departureDelay: Optional[datetime.timedelta]
    :ivar departurePlatform: Real-time departure platform at the station (maybe `None`)
    :vartype departurePlatform: Optional[str]
    :ivar remarks: (optional) List of remarks
    :vartype remarks: List[Remark]
    """

    def __init__(
            self,
            stop: Station,
            cancelled: bool = False,
            arrival: Optional[datetime.datetime] = None,
            arrival_delay: Optional[datetime.timedelta] = None,
            arrival_platform: Optional[str] = None,
            departure: Optional[datetime.datetime] = None,
            departure_delay: Optional[datetime.timedelta] = None,
            departure_platform: Optional[str] = None,
            remarks: Optional[List[Remark]] = None
    ):
        """

        :param stop: Station where the vehicle is stopping
        :param cancelled: (optional) Whether the stop is cancelled. Defaults to `False`
        :param arrival: (optional) Planned arrival date and time at the station. Defaults to `None`
        :param arrival_delay: (optional) Arrival delay at the station. Defaults to `None`
        :param arrival_platform: (optional) Real-time arrival platform at the station. Defaults to `None`
        :param departure: (optional) Planned departure date and time at the station. Defaults to `None`
        :param departure_delay: (optional) Departure delay at the station. Defaults to `None`
        :param departure_platform: (optional) Real-time departure platform at the station. Defaults to `None`
        :param remarks: (optional) List of remarks. Defaults to `[]`
        """
        self.stop: Station = stop
        self.cancelled: bool = cancelled
        self.arrival: Optional[datetime.datetime] = arrival
        self.arrivalDelay: Optional[datetime.timedelta] = arrival_delay
        self.arrivalPlatform: Optional[str] = arrival_platform
        self.departure: Optional[datetime.datetime] = departure
        self.departureDelay: Optional[datetime.timedelta] = departure_delay
        self.departurePlatform: Optional[str] = departure_platform
        if remarks is None:
            remarks = []
        self.remarks: List[Remark] = remarks


class Leg(FPTFObject):
    """
    FPTF `Leg` object

    A leg or also named trip is most times part of a journey and defines a journey with only one specific vehicle from A to B.

    :ivar id: ID of the Leg
    :vartype id: str
    :ivar origin: FPTF `Station` object of the origin station
    :vartype origin: Station
    :ivar destination: FPTF `Station` object of the destination station
    :vartype destination: Station
    :ivar departure: Planned Date and Time of the departure
    :vartype departure: datetime.datetime
    :ivar arrival: Planned Date and Time of the arrival
    :vartype arrival: datetime.datetime
    :ivar mode: Type of transport vehicle - Must be a part of the FPTF `Mode` enum. Defaults to `Mode.TRAIN`
    :vartype mode: Mode
    :ivar name: Name of the trip (e.g. ICE 123) (maybe `None`)
    :vartype name: Optional[str]
    :ivar cancelled: Whether the trip is completely cancelled (not only some stops)
    :vartype cancelled: bool
    :ivar distance: Distance of the walk trip in metres. Only set if `mode` is `Mode.WALKING` otherwise None
    :vartype distance: Optional[int]
    :ivar departureDelay: Delay at the departure station (maybe `None`)
    :vartype departureDelay: Optional[datetime.timedelta]
    :ivar departurePlatform: Real-time platform at the departure station (maybe `None`)
    :vartype departurePlatform: Optional[str]
    :ivar arrivalDelay: Delay at the arrival station (maybe `None`)
    :vartype arrivalDelay: Optional[datetime.timedelta]
    :ivar arrivalPlatform: Real-time platform at the arrival station (maybe `None`)
    :vartype arrivalPlatform: Optional[str]
    :ivar stopovers: List of FPTF `Stopover` objects (maybe `None`)
    :vartype stopovers: Optional[List[Stopover]]
    :ivar remarks: (optional) List of remarks
    :vartype remarks: List[Remark]
    """

    def __init__(
            self,
            id: str,
            origin: Station,
            destination: Station,
            departure: datetime.datetime,
            arrival: datetime.datetime,
            mode: Mode = Mode.TRAIN,
            name: Optional[str] = None,
            additional_name: Optional[str] = None,
            cancelled: bool = False,
            distance: Optional[int] = None,
            departure_delay: Optional[datetime.timedelta] = None,
            departure_platform: Optional[str] = None,
            arrival_delay: Optional[datetime.timedelta] = None,
            arrival_platform: Optional[str] = None,
            stopovers: Optional[List[Stopover]] = None,
            remarks: Optional[List[Remark]] = None
    ):
        """
        FPTF `Leg` object

        :param id: Internal ID of the station
        :param origin: FPTF `Station` object of the origin station
        :param destination: FPTF `Station` object of the destination station
        :param departure: Planned date and Time of the departure
        :param arrival: Planned date and Time of the arrival
        :param mode: (optional) Type of transport vehicle - Must be a part of the FPTF `Mode` enum. Defaults to `Mode.TRAIN`
        :param name: (optional) Name of the trip (e.g. RE 10354). Defaults to None
        :param additional_name: (optional) Additional name of the trip (e.g. RE 4). Defaults to None
        :param cancelled: (optional) Whether the trip is cancelled. Defaults to False
        :param distance: (optional) Distance of the walk trip in meters. Defaults to None
        :param departure_delay: (optional) Delay at the departure station. Defaults to None
        :param departure_platform: (optional) Real-time platform at the departure station. Defaults to None
        :param arrival_delay: (optional) Delay at the arrival station. Defaults to None
        :param arrival_platform: (optional) Platform at the arrival station. Defaults to None
        :param stopovers: (optional) List of FPTF `Stopover` objects. Defaults to None
        :param remarks: (optional) List of remarks. Defaults to `[]`
        """
        # Mandatory Variables
        self.id = id
        self.origin: Station = origin
        self.destination: Station = destination
        self.departure: datetime.datetime = departure
        self.arrival: datetime.datetime = arrival

        # Optional Variables
        self.mode: Mode = mode
        self.name: Optional[str] = name
        self.additionalName: Optional[str] = additional_name
        self.cancelled: bool = cancelled
        self.distance: Optional[int] = distance
        self.departureDelay: Optional[datetime.timedelta] = departure_delay
        self.departurePlatform: Optional[str] = departure_platform
        self.arrivalDelay: Optional[datetime.timedelta] = arrival_delay
        self.arrivalPlatform: Optional[str] = arrival_platform
        self.stopovers: Optional[List[Stopover]] = stopovers
        if remarks is None:
            remarks = []
        self.remarks: List[Remark] = remarks


class Journey(FPTFObject):
    """
    FPTF `Journey` object

    A journey is a computed set of directions to get from A to B at a specific time. It would typically be the result of a route planning algorithm.

    :ivar id: ID of the Journey
    :vartype id: str
    :ivar date: Starting date of the journey (maybe `None`)
    :vartype date: Optional[datetime.date]
    :ivar duration: Duration of the complete journey (maybe `None`)
    :vartype duration: Optional[datetime.timedelta]
    :ivar legs: Longitude coordinate of the Station (maybe `None`)
    :vartype legs: Optional[List[Leg]]
    """

    def __init__(
            self,
            id: str,
            date: Optional[datetime.date] = None,
            duration: Optional[datetime.timedelta] = None,
            legs: Optional[List[Leg]] = None):
        """
        FPTF `Journey` object

        :param id: Internal ID of the station
        :param date: (optional) Name of the station
        :param duration: (optional) Latitude coordinate of the station. Defaults to None
        :param legs: (optional) Longitude coordinate of the station. Defaults to None
        """
        self.id: str = id
        self.date: Optional[datetime.date] = date
        self.duration: Optional[datetime.timedelta] = duration
        self.legs: Optional[List[Leg]] = legs


class StationBoardLeg(FPTFObject):
    """
    `StationBoardLeg` object

    Returned at Station Board-Requests. This requests do not have enough information for a FPTF `Leg` object.
    With the ID a `trip` request can be made to get detailed information about the trip

    :ivar id: ID of the Leg
    :vartype id: str
    :ivar name: Name of the trip (e.g. ICE 123)
    :vartype name: str
    :ivar station: FPTF `Station` object of the departing/arriving station
    :vartype station: Station
    :ivar date_time: Planned Date and Time of the departure/arrival
    :vartype date_time: datetime.datetime
    :ivar cancelled: Whether the stop or trip cancelled
    :vartype cancelled: bool
    :ivar direction: Direction text of the trip (e.g. Berlin Central Station)
    :vartype direction: Optional[str]
    :ivar delay: Delay at the departure station (maybe `None`)
    :vartype delay: Optional[datetime.timedelta]
    :ivar platform: Real-time platform at the station (maybe `None`)
    :vartype platform: Optional[str]
    """

    def __init__(
            self,
            id: str,
            name: str,
            station: Station,
            date_time: datetime.datetime,
            cancelled: bool,
            direction: Optional[str] = None,
            delay: Optional[datetime.timedelta] = None,
            platform: Optional[str] = None,
            additional_name: Optional[str] = None,

    ):
        """
        `StationBoardLeg` object

        :param id: ID of the Leg
        :param name: Name of the trip (e.g. ICE 123)
        :param station: FPTF `Station` object of the departing/arriving station
        :param date_time: Planned Date and Time of the departure/arrival
        :param cancelled: Whether the stop or trip cancelled
        :param direction: (optional) Direction text of the trip (e.g. Berlin Central Station)
        :param delay: (optional) Delay at the departure station. Defaults to `None`
        :param platform: (optional) Real-time platform at the station. Defaults to `None`
        :param additional_name: (optional) Additional name if available (e.g. RE 4)
        """
        self.id: str = id
        self.name: str = name
        self.station: Station = station
        self.dateTime: datetime.datetime = date_time
        self.cancelled: bool = cancelled
        self.direction: Optional[str] = direction
        self.delay: Optional[datetime.timedelta] = delay
        self.platform: Optional[str] = platform
        self.additionalName: str = additional_name
