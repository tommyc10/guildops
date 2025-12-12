# backend/app/models/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Mission(Base):
    __tablename__ = "missions"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Core Brief
    title = Column(String, index=True) # e.g. "Capture Han Solo"
    objective = Column(Text)           # e.g. "Bring him in warm, or cold."
    target = Column(String)
    location = Column(String)          # e.g. "Bespin"
    
    # Constraints & Details
    constraints = Column(JSON)         # List of strings e.g. ["No disintegrations"]
    budget = Column(Integer)           # Credits
    timeframe = Column(String)         # e.g. "1 week"
    tone = Column(String, default="formal") # "formal" or "blunt"
    
    # Status tracking
    status = Column(String, default="draft") # draft -> planned -> critiqued
    
    # Timestamps (Server default ensures DB handles the time)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship to PlanVersion
    # 'back_populates' links this to the parent field in PlanVersion
    plans = relationship("PlanVersion", back_populates="mission", cascade="all, delete-orphan")


class PlanVersion(Base):
    __tablename__ = "plan_versions"

    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign Key linking to Mission
    mission_id = Column(Integer, ForeignKey("missions.id"))
    
    version = Column(Integer, default=1)
    
    # AI Generated Content
    summary = Column(Text)
    steps = Column(JSON)      # Structured timeline
    risks = Column(JSON)      # Risk analysis objects
    gear = Column(JSON)       # Loadout checklist
    transport = Column(String)
    
    critique_notes = Column(Text, nullable=True) # If this plan was a result of feedback
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship back to Mission
    mission = relationship("Mission", back_populates="plans")