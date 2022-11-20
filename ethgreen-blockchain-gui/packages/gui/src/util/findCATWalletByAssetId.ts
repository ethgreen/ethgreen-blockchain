import type { Wallet } from '@ethgreen/api';
import { WalletType } from '@ethgreen/api';

export default function findCATWalletByAssetId(
  wallets: Wallet[],
  assetId: string,
) {
  return wallets.find(
    (wallet) =>
      wallet.type === WalletType.CAT &&
      wallet.meta?.assetId?.toLowerCase() === assetId.toLowerCase(),
  );
}
