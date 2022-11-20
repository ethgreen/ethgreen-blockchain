import { useMemo } from 'react';
import type { Wallet } from '@ethgreen/api';
import { WalletType } from '@ethgreen/api';
import BigNumber from 'bignumber.js';
import { mojoToCATLocaleString, mojoToETHgreenLocaleString, useLocale } from '@ethgreen/core';

export default function useWalletHumanValue(wallet: Wallet, value?: string | number | BigNumber, unit?: string): string {
  const [locale] = useLocale();
  
  return useMemo(() => {
    if (wallet && value !== undefined) {
      const localisedValue = wallet.type === WalletType.CAT
        ? mojoToCATLocaleString(value, locale)
        : mojoToETHgreenLocaleString(value, locale);

      return `${localisedValue} ${unit}`;
    }

    return '';
  }, [wallet, value, unit, locale]);
}
