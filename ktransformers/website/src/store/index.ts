import { createStore } from 'vuex'

interface User {
  id: number;
  username: string;
  email: string | null;
  is_active: boolean;
  created_at: number;
}

interface State {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
}

export default createStore<State>({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
    isAuthenticated: !!localStorage.getItem('token'),
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    currentUser: (state) => state.user,
    token: (state) => state.token,
  },
  mutations: {
    setAuth(state, { token, user }) {
      state.token = token;
      state.user = user;
      state.isAuthenticated = true;
      localStorage.setItem('token', token);
    },
    clearAuth(state) {
      state.token = null;
      state.user = null;
      state.isAuthenticated = false;
      localStorage.removeItem('token');
    },
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    login({ commit }, { token, user }) {
      commit('setAuth', { token, user });
    },
    logout({ commit }) {
      commit('clearAuth');
    },
    setUser({ commit }, user) {
      commit('setUser', user);
    },
  },
  modules: {
  }
})

