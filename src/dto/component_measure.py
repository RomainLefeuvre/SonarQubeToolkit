from dataclasses import dataclass
from typing import Optional, List


@dataclass
class MeasurePeriod:
    value: int
    best_value: bool


@dataclass
class Measure:
    metric: str
    period: MeasurePeriod
    value: Optional[int] = None

@dataclass
class Component:
    key: str
    name: str
    qualifier: str
    language: str
    path: str
    measures: List[Measure]


@dataclass
class Metric:
    key: str
    name: str
    description: str
    domain: str
    type: str
    higher_values_are_better: bool
    qualitative: bool
    hidden: bool


@dataclass
class Period:
    mode: str
    date: str
    parameter: str


@dataclass
class ComponentMeasureDTO:
    component: Component
    metrics: List[Metric]
    period: Period