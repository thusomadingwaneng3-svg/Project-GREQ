"""
PROJECT GREQ: THE GLOBAL RESOURCE EQUALIZER
A decentralized system to bridge human needs and surplus without money.
"""

import hashlib
import time
import datetime
import zlib

class ProjectGREQ:
    def __init__(self):
        # 1. Database of users and their reputations
        self.registry = {"FOUNDER_01": {"score": 1.0, "vouched_by": None}}
        
        # 2. Database of available resources (Skills/Items)
        self.network_mesh = {}
        
        # 3. List of active community needs
        self.active_imbalances = []
        
        # 4. Offline Knowledge Library
        self.library = {
            "water_purification": "1. Filter through sand. 2. Boil for 1 min. 3. Store in clean vessel.",
            "basic_first_aid": "Stop bleeding with pressure. Elevate limbs. Keep patient warm.",
            "soil_health": "Use compost and crop rotation to restore nitrogen levels."
        }

    # --- THE VOUCH SYSTEM ---
    def add_user(self, inviter_id, new_user_id):
        if inviter_id not in self.registry:
            return "❌ Error: Inviter not found in network."
        if self.registry[inviter_id]["score"] < 0.8:
            return "❌ Access Denied: Inviter trust score too low."
        
        self.registry[new_user_id] = {
            "score": 0.5, # Probationary score
            "vouched_by": inviter_id,
            "status": "active"
        }
        return f"✅ User {new_user_id} joined. Welcome to the Mesh."

    # --- THE RESOURCE MESH ---
    def list_surplus(self, user_id, r_type, description):
        entry_id = hashlib.sha256(f"{user_id}{time.time()}".encode()).hexdigest()[:8]
        self.network_mesh[entry_id] = {
            "provider": user_id,
            "type": r_type,
            "desc": description,
            "status": "available"
        }
        return f"✅ Listed {r_type}: {description} (ID: {entry_id})"

    # --- THE NEEDS BROADCAST ---
    def report_need(self, user_id, category, details, urgency):
        imbalance = {
            "user": user_id,
            "cat": category,
            "desc": details,
            "priority": urgency, # 1 is high
            "time": datetime.datetime.now()
        }
        self.active_imbalances.append(imbalance)
        return "🚨 Need broadcasted to local mesh neighbors."

    # --- THE KNOWLEDGE SEED ---
    def share_knowledge(self, topic):
        if topic in self.library:
            # Compress to keep it tiny for offline sharing
            data = zlib.compress(self.library[topic].encode())
            return f"📦 Knowledge Seed for '{topic}' ready for P2P transfer ({len(data)} bytes)."
        return "❌ Topic not found in library."

# --- STARTING THE ENGINE ---
greq = ProjectGREQ()

# 1. Join the network
print(greq.add_user("FOUNDER_01", "You_The_Founder"))

# 2. List what you can offer the world
print(greq.list_surplus("You_The_Founder", "Skills", "I can teach Python coding"))

# 3. Report a local community need
print(greq.report_need("You_The_Founder", "Tools", "Need a 3D printer for medical parts", 2))

# 4. Access life-saving info offline
print(greq.share_knowledge("water_purification"))
