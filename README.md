# Python Game Menu & Runtime Systems Simulation 

This is a console-based game framework that has been built in Python that simulates real world game systems such as:
1) Menus
2) Settings
3) runtime performance changes
4) audio stress
5) debugging overlays

The project focuses mainly on **game ready architecture and systems design**, not graphics. This further demonstrates how game engines manage states, performance, and user settings at runtime. 

## Features 

### Menu & State Managment 
- State driven architecture using enum variables
- Main Menu, Settings, Pause Menu and Confirm Quit
- Clean State Transitions with State Handler Mapping
- Safe handling of invalid or any unexpected States

### Runtime Settings Systems 
- Consistent and presistent settings saved to disk (via 'settings.json')
- Live applications of settings during gameplay
- In-Game settings that are accessible via pause menu
- Settings affect performance and/or audio behavior

### Audio System Simulation 
- Audio Crackle and distortion based feedback on performance stress
- Volume-based audio like behavior 
- Audio recovery system after performance has been stabilized
- Simulation of buffer underruns and overall recovery states

### Debugging and Development Tools 
- Toggle the debug overlay display via (d) button 
- Live FPS, tick counting, and systems state display
- Designed to resemble diagnostic tools that are found in engine

## Technical Concepts that were demonstrated 
- Finite State Machines
- Separation of concerns
- Runtime Config. Systems
- Defensive programming
- Game loop sim.
- Performance modeling
- Debug tool design


## Tech Used 
- Python 3
- Enum-based state management
- JSON (used mainly for settings)
- Colorama for UI Feedback 
