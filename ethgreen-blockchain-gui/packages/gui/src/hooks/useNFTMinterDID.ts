import { useMemo } from 'react';
import { useGetNFTInfoQuery } from '@ethgreen/api-react';
import { launcherIdFromNFTId } from '../util/nfts';
import { stripHexPrefix } from '../util/utils';
import { didToDIDId } from '../util/dids';

export type UseNFTMinterDIDResult = {
  didId: string | undefined;
  hexDIDId: string | undefined;
  didName: string | undefined;
  isLoading: boolean;
  error: Error | undefined;
};

export default function useNFTMinterDID(nftId: string): UseNFTMinterDIDResult {
  const launcherId = launcherIdFromNFTId(nftId);
  const {
    data: nft,
    isLoading,
    error,
  } = useGetNFTInfoQuery({ coinId: launcherId ?? '' });

  const [didId, hexDIDId, didName] = useMemo(() => {
    if (!nft) {
      return [];
    }
    const { minterDid } = nft;
    if (!minterDid) {
      return [];
    }
    const hexDIDId = stripHexPrefix(minterDid);
    const didId = didToDIDId(hexDIDId);
    let didName;

    return [didId, hexDIDId, didName];
  }, [nft]);

  return { didId, hexDIDId, didName, isLoading, error };
}
