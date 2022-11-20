import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import ethgreenFormatter from './ethgreenFormatter';

export default function catToMojo(cat: string | number | BigNumber): BigNumber {
  return ethgreenFormatter(cat, Unit.CAT)
    .to(Unit.MOJO)
    .toBigNumber();
}