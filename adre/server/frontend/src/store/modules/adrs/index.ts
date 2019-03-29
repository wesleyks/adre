import {
  getModule,
  Module,
  VuexModule,
  MutationAction,
} from 'vuex-module-decorators';

import store from '@/store';
import adrAPI from '@/api/adrs';

import { ADR, RawADR, Tag, RawTag } from './types';

@Module({
  name: 'adrs',
  namespaced: true,
  dynamic: true,
  store,
})
class ADRsModule extends VuexModule {
  public adrs: ADR[] = [];

  get adrsById() {
    const adrs: { [id: number]: ADR } = {};
    return this.adrs.reduce((accum, adr) => {
      accum[adr.id] = adr;
      return accum;
    }, adrs);
  }

  @MutationAction
  public async loadADRs() {
    const response = await adrAPI.getADRs();
    return {
      adrs: response.data.adrs.map((adr: RawADR) => {
        return {
          ...adr,
          tags: adr.tags.map((tag: RawTag) => {
            return tag.split('.');
          }),
        };
      }),
    };
  }
}

export default getModule(ADRsModule);
