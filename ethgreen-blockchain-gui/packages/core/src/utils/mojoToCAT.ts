import BigNumber from 'bignumber.js';
import Unit from '../constants/Unit';
import ethgreenFormatter from './ethgreenFormatter';

export default function mojoToCAT(mojo: string | number | BigNumber): BigNumber {
  return ethgreenFormatter(mojo, Unit.MOJO)
    .to(Unit.CAT)
    .toBigNumber();
}