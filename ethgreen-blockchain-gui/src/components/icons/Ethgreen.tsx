import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as EthgreenIcon } from './images/ethgreen.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={EthgreenIcon} viewBox="0 0 160 53" {...props} />;
}
