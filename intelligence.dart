class GreqIntelligence {
  // A local, high-speed index of survival knowledge
  static final Map<String, String> _knowledgeBase = {
    "hunger": "Check local mesh for food surplus or use Seed #402: Urban Foraging.",
    "energy": "Seed #109: Building a DIY Solar Heater from recycled cans.",
    "water": "Seed #001: Biosand filtration systems for community health.",
  };

  static String consult(String query) {
    String lowerQuery = query.toLowerCase();
    for (var key in _knowledgeBase.keys) {
      if (lowerQuery.contains(key)) return _knowledgeBase[key]!;
    }
    return "Analyzing local mesh for answers... No offline seed found. Try broadcasting this need.";
  }
}
