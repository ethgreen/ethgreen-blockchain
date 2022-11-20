import React from 'react';
import styled from 'styled-components';
import { Box, BoxProps } from '@mui/material';
import { ETHgreen } from '@ethgreen/icons';

const StyledETHgreen = styled(ETHgreen)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledETHgreen />
    </Box>
  );
}
