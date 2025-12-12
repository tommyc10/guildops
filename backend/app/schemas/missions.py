# backend/app/schemas/missions.py

from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Any
from datetime import datetime

# --- PLAN SCHEMAS ---
# We define these first so Mission can reference them

class PlanBase(BaseModel):
    # These are fields we might eventually allow updating
    summary: Optional[str] = None
    transport: Optional[str] = None

class PlanRead(PlanBase):
    """How a plan looks when reading it from the API"""
    id: int
    version: int
    steps: Optional[List[Any]] = None  # JSON content
    risks: Optional[List[Any]] = None  # JSON content
    gear: Optional[List[Any]] = None   # JSON content
    critique_notes: Optional[str] = None
    created_at: datetime

    # This config tells Pydantic: "It's okay to read data from a SQLAlchemy model"
    model_config = ConfigDict(from_attributes=True)


# --- MISSION SCHEMAS ---

class MissionBase(BaseModel):
    """Shared properties for creating and reading"""
    title: str
    objective: str
    target: str
    location: str
    constraints: List[str] = [] # Default to empty list
    budget: int
    timeframe: str
    tone: str = "formal" # Default tone

class MissionCreate(MissionBase):
    """
    Validation for creating a new mission.
    We inherit everything from Base. 
    User doesn't send ID or status; we handle those.
    """
    pass

class MissionUpdate(MissionBase):
    """Fields that can be updated (all optional)"""
    title: Optional[str] = None
    objective: Optional[str] = None
    target: Optional[str] = None
    location: Optional[str] = None
    budget: Optional[int] = None
    timeframe: Optional[str] = None

class MissionRead(MissionBase):
    """
    The full response object. 
    Includes DB-generated fields like ID and timestamps.
    """
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    # Nested relationship: Include the list of plans!
    plans: List[PlanRead] = []

    model_config = ConfigDict(from_attributes=True)