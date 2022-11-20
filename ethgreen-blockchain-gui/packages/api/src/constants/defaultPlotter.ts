import PlotterName from './PlotterName';
import optionsForPlotter from '../utils/optionsForPlotter';
import defaultsForPlotter from '../utils/defaultsForPlotter';

export default {
  displayName: 'ETHgreen Proof of Space',
  options: optionsForPlotter(PlotterName.ETHGREENPOS),
  defaults: defaultsForPlotter(PlotterName.ETHGREENPOS),
  installInfo: { installed: true },
};
