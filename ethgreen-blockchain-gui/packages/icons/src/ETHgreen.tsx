import React from 'react';
import { SvgIcon, SvgIconProps } from '@mui/material';
import ETHgreenIcon from './images/ethgreen.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={ETHgreenIcon} viewBox="0 0 150 58" {...props} />;
}
