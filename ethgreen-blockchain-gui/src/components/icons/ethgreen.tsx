import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as ethgreenIcon } from './images/ethgreen.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={ethgreenIcon} viewBox="0 0 150 58" {...props} />;
}
