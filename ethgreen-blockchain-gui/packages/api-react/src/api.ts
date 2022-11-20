import { createApi } from '@reduxjs/toolkit/query/react';
import ethgreenLazyBaseQuery from './ethgreenLazyBaseQuery';

export const baseQuery = ethgreenLazyBaseQuery({});

export default createApi({
  reducerPath: 'ethgreenApi',
  baseQuery,
  endpoints: () => ({}),
});
