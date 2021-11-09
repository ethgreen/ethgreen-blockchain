export const service_wallet = 'ethgreen_wallet';
export const service_full_node = 'ethgreen_full_node';
export const service_farmer = 'ethgreen_farmer';
export const service_harvester = 'ethgreen_harvester';
export const service_simulator = 'ethgreen_full_node_simulator';
export const service_daemon = 'daemon';
export const service_plotter = 'ethgreen plots create';

// Corresponds with outbound_message.py NodeTypes
export const service_connection_types = {
  1: 'Full Node',
  2: 'Harvester',
  3: 'Farmer',
  4: 'Timelord',
  5: 'Introducer',
  6: 'Wallet',
  7: 'Plotter',
};
