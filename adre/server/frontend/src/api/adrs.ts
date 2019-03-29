import axios from 'axios';

const client = axios.create({
  baseURL: process.env.VUE_APP_API_ENDPOINT,
});

export default {
  getADRs() {
    return client.get('/adrs');
  },
};
