# Athena Integration for Home Assistant

A custom integration for Home Assistant that provides support for Athena monitoring and control systems.

## Features

- **Sensors**: Temperature, Humidity, Pressure, Signal Strength, Status monitoring
- **Switches**: Power control, Auto mode switching
- **Binary Sensors**: Online status, Fault detection, Maintenance mode
- **Number Entities**: Configurable thresholds and intervals
- **Select Entities**: Mode and profile selection
- **Real-time Monitoring**: Continuous data updates with configurable intervals

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL and select "Integration" as category
6. Click "Add"
7. Find "Athena" in the integration list and install it
8. Restart Home Assistant

### Manual Installation

1. Download the `athena` folder from this repository
2. Copy it to your `custom_components` directory in your Home Assistant configuration
3. Restart Home Assistant

## Configuration

1. Go to Settings → Devices & Services
2. Click "Add Integration"
3. Search for "Athena"
4. Follow the configuration wizard:
   - Enter your device's IP address or hostname
   - Set the port (default: 80)
   - Provide authentication credentials
   - Select device type (Controller, Monitor, or Sensor)
   - Configure scan interval (default: 30 seconds)

## Supported Entities

### Sensors
- **Temperature**: Current temperature reading
- **Humidity**: Relative humidity percentage
- **Pressure**: Atmospheric pressure
- **Signal Strength**: Device signal strength in dBm
- **Status**: Current device status

### Switches
- **Power**: Main power control
- **Auto Mode**: Automatic operation mode

### Binary Sensors
- **Online**: Device connectivity status
- **Fault**: Fault detection indicator
- **Maintenance**: Maintenance mode status

### Configuration Entities
- **Threshold**: Configurable threshold values
- **Interval**: Update interval settings
- **Mode**: Operation mode selection
- **Profile**: Device profile selection

## Device Types

- **Controller**: Full control capabilities with all entities
- **Monitor**: Read-only monitoring with sensors and binary sensors
- **Sensor**: Basic sensor data only

## Troubleshooting

### Connection Issues
- Verify the device IP address and port
- Check network connectivity
- Ensure authentication credentials are correct

### Missing Entities
- Restart Home Assistant after installation
- Check the device type configuration
- Verify device firmware compatibility

### Update Issues
- Clear browser cache
- Restart Home Assistant
- Check HACS for integration updates

## Support

For issues and feature requests, please use the [GitHub Issues](https://github.com/your-username/athena-integration/issues) page.

## Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
