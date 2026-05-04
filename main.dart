import 'package:flutter/material.dart';

void main() => runApp(ProjectGREQApp());

class ProjectGREQApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Project GREQ',
      theme: ThemeData(primarySwatch: Colors.teal),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _selectedIndex = 0;
  
  // Simulated Trust Score
  double trustScore = 0.85;

  static List<Widget> _pages = <Widget>[
    BroadcastPage(),
    MeshMapPage(),
    KnowledgeLibraryPage(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('🌍 GREQ: Global Mesh')),
      body: _pages[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (index) => setState(() => _selectedIndex = index),
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.broadcast_on_home), label: 'Broadcast'),
          BottomNavigationBarItem(icon: Icon(Icons.map), label: 'Local Mesh'),
          BottomNavigationBarItem(icon: Icon(Icons.book), label: 'Knowledge'),
        ],
      ),
    );
  }
}

// Placeholder pages for you to expand
class BroadcastPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Center(child: Text("Post Surplus or Needs Here"));
}
class MeshMapPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Center(child: Text("Real-time Local Resource Map"));
}
class KnowledgeLibraryPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Center(child: Text("Offline 'Seeds' Library"));
}
