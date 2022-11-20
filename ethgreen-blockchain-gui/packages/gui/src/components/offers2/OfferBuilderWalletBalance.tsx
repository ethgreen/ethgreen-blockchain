import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { WalletType } from '@ethgreen/api';
import { useGetWalletBalanceQuery } from '@ethgreen/api-react';
import {
  FormatLargeNumber,
  mojoToCATLocaleString,
  mojoToETHgreenLocaleString,
  useLocale,
} from '@ethgreen/core';
import { useWallet } from '@ethgreen/wallets';

export type OfferBuilderWalletBalanceProps = {
  walletId: number;
};

export default function OfferBuilderWalletBalance(
  props: OfferBuilderWalletBalanceProps,
) {
  const { walletId } = props;
  const [locale] = useLocale();
  const { data: walletBalance, isLoading: isLoadingWalletBalance } =
    useGetWalletBalanceQuery({
      walletId,
    });

  const { unit, wallet, loading } = useWallet(walletId);

  const isLoading = isLoadingWalletBalance || loading;

  const xfxBalance = useMemo(() => {
    if (
      isLoading ||
      !wallet ||
      !walletBalance ||
      !('spendableBalance' in walletBalance)
    ) {
      return undefined;
    }

    if (wallet.type === WalletType.STANDARD_WALLET) {
      return mojoToETHgreenLocaleString(walletBalance.spendableBalance, locale);
    }

    if (wallet.type === WalletType.CAT) {
      return mojoToCATLocaleString(walletBalance.spendableBalance, locale);
    }

    return undefined;
  }, [
    isLoading,
    wallet,
    walletBalance,
    walletBalance?.spendableBalance,
    locale,
  ]);

  if (!isLoading && xfxBalance === undefined) {
    return null;
  }

  return (
    <Trans>
      Spendable Balance:{' '}
      {isLoading ? (
        'Loading...'
      ) : (
        <>
          {xfxBalance}
          &nbsp;
          {unit?.toUpperCase()}
        </>
      )}
    </Trans>
  );
}
