import { createContext } from 'react';
import type { CalculateRoyaltiesResponse } from '@ethgreen/api';
import OfferState from '../offers/OfferState';

export interface OfferBuilderContextData {
  readOnly: boolean;
  imported: boolean;
  isMyOffer: boolean;
  state?: OfferState;
  offeredUnknownCATs?: string[];
  requestedUnknownCATs?: string[];
  usedAssetIds: string[];
  royalties?: CalculateRoyaltiesResponse;
  isCalculatingRoyalties: boolean;
}

const OfferBuilderContext = createContext<OfferBuilderContextData | undefined>(
  undefined,
);

export default OfferBuilderContext;
