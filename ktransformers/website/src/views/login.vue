<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-header">
        <h2>{{ isRegisterMode ? $t('login.register') : $t('login.signIn') }}</h2>
      </div>
      <el-form :model="form" :rules="rules" ref="loginForm" class="login-form">
        <el-form-item prop="username">
          <el-input
            v-model="form.username"
            :placeholder="$t('login.username')"
            prefix-icon="User"
          />
        </el-form-item>
        <el-form-item prop="email" v-if="isRegisterMode">
          <el-input
            v-model="form.email"
            :placeholder="$t('login.email')"
            prefix-icon="Message"
          />
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="form.password"
            type="password"
            :placeholder="$t('login.password')"
            prefix-icon="Lock"
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="handleSubmit"
            :loading="loading"
            class="login-button"
          >
            {{ isRegisterMode ? $t('login.register') : $t('login.signIn') }}
          </el-button>
        </el-form-item>
        <div class="switch-mode">
          <span @click="toggleMode" class="switch-link">
            {{ isRegisterMode ? $t('login.haveAccount') : $t('login.noAccount') }}
          </span>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';
import { login, register, getCurrentUser } from '@/api/auth';

export default defineComponent({
  name: 'LoginView',
  setup() {
    const router = useRouter();
    const store = useStore();
    const loginForm = ref();
    const loading = ref(false);
    const isRegisterMode = ref(false);
    
    const form = ref({
      username: '',
      email: '',
      password: '',
    });

    const rules = {
      username: [
        { required: true, message: 'Please input username', trigger: 'blur' },
        { min: 3, max: 20, message: 'Length should be 3 to 20', trigger: 'blur' },
      ],
      password: [
        { required: true, message: 'Please input password', trigger: 'blur' },
        { min: 6, message: 'Password should be at least 6 characters', trigger: 'blur' },
      ],
    };

    const toggleMode = () => {
      isRegisterMode.value = !isRegisterMode.value;
      form.value.email = '';
    };

    const handleSubmit = async () => {
      if (!loginForm.value) return;
      
      await loginForm.value.validate(async (valid: boolean) => {
        if (!valid) return;
        
        loading.value = true;
        try {
          if (isRegisterMode.value) {
            // Register
            await register({
              username: form.value.username,
              password: form.value.password,
              email: form.value.email || undefined,
            });
            ElMessage.success('Registration successful! Please login.');
            isRegisterMode.value = false;
          } else {
            // Login
            const authResponse = await login({
              username: form.value.username,
              password: form.value.password,
            });
            
            // Store token first so the interceptor can use it
            store.dispatch('login', {
              token: authResponse.access_token,
              user: null,
            });
            
            // Get user info (will use the token from store via interceptor)
            const user = await getCurrentUser();
            
            // Update user info in store
            store.dispatch('setUser', user);
            
            ElMessage.success('Login successful!');
            router.push('/');
          }
        } catch (error: any) {
          const message = error.response?.data?.detail || 'Operation failed';
          ElMessage.error(message);
        } finally {
          loading.value = false;
        }
      });
    };

    return {
      form,
      rules,
      loginForm,
      loading,
      isRegisterMode,
      toggleMode,
      handleSubmit,
    };
  },
});
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.login-box {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  width: 400px;
}

.login-header {
  text-align: center;
  margin-bottom: 30px;
}

.login-header h2 {
  color: #333;
  margin: 0;
}

.login-form {
  width: 100%;
}

.login-button {
  width: 100%;
}

.switch-mode {
  text-align: center;
  margin-top: 10px;
}

.switch-link {
  color: #667eea;
  cursor: pointer;
  font-size: 14px;
}

.switch-link:hover {
  text-decoration: underline;
}
</style>
