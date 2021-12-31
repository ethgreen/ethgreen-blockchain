import React from 'react';
import styled from 'styled-components';
import { Box, BoxProps } from '@material-ui/core';
import { Ethgreen } from '@ethgreen/icons';

const StyledEthgreen = styled(Ethgreen)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledEthgreen />
    </Box>
  );
}
