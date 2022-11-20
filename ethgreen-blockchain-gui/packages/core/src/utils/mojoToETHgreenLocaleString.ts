import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import ethgreenFormatter from './ethgreenFormatter';

export default function mojoToETHgreenLocaleString(mojo: string | number | BigNumber, locale?: string) {
  return ethgreenFormatter(mojo, Unit.MOJO)
    .to(Unit.ETHGREEN)
    .toLocaleString(locale);
}
