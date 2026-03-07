import api from './api';

export const addAsset = (asset) => {
    return api.post('/asset/add', asset).then(res => res.data);
};
