import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import ethgreenFormatter from './ethgreenFormatter';

export default function ethgreenToMojo(ethgreen: string | number | BigNumber): BigNumber {
  return ethgreenFormatter(ethgreen, Unit.ETHGREEN)
    .to(Unit.MOJO)
    .toBigNumber();
}