import Vue from 'vue';
import Vuex from 'vuex';

import adrs from './modules/adrs';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    adrs,
  },
});
