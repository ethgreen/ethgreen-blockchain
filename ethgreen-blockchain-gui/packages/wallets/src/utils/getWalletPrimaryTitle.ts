import { WalletType } from '@ethgreen/api';
import type { Wallet } from '@ethgreen/api';

export default function getWalletPrimaryTitle(wallet: Wallet): string {
  switch (wallet.type) {
    case WalletType.STANDARD_WALLET:
      return 'ETHgreen';
    default:
      return wallet.meta?.name ?? wallet.name;
  }
}
