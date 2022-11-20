import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useCurrencyCode, mojoToETHgreenLocaleString, CardSimple, useLocale } from '@ethgreen/core';
import { useGetFarmedAmountQuery } from '@ethgreen/api-react';

export default function FarmCardTotalETHgreenFarmed() {
  const currencyCode = useCurrencyCode();
  const [locale] = useLocale();
  const { data, isLoading, error } = useGetFarmedAmountQuery();

  const farmedAmount = data?.farmedAmount;

  const totalETHgreenFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      return (
        <>
          {mojoToETHgreenLocaleString(farmedAmount, locale)}
          &nbsp;
          {currencyCode}
        </>
      );
    }
  }, [farmedAmount, locale, currencyCode]);

  return (
    <CardSimple
      title={<Trans>Total ETHgreen Farmed</Trans>}
      value={totalETHgreenFarmed}
      loading={isLoading}
      error={error}
    />
  );
}
