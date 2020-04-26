<template>
  <el-row>
    <el-col :xs="4"
            :sm="4"
            :md="6"
            :lg="8"
            :xl="8"
            class="title">Tasaka</el-col>
    <el-col :xs="4"
            :sm="4"
            :md="6"
            :lg="8"
            :xl="8"
            class="title">&nbsp;</el-col>
    <el-col :xs="16"
            :sm="16"
            :md="14"
            :lg="12"
            :xl="12"
            class="rightbar">
      <div v-for="(item, index) in tabtitle"
           :key="index"
           @click="handle(index)"
           :class="currentIndex === index ? 'active' : ''">
        {{item}}
      </div>
      <el-button size="small"
                 plain
                 @click="drawer = true">登陆/注册</el-button>
    </el-col>
    <el-drawer @close="closeDrawer"
               size="75%"
               :visible.sync="drawer">
      <div class="tabs">
        <div v-for="(item, index) in lr"
             :key="item"
             :class="lrIndex == index? 'lractive':''"
             @click="clickLR(index)">{{item}}</div>
      </div>

      <el-form ref="loginForm"
               :model="loginForm"
               :rules="loginRules"
               label-position="left"
               v-show="lrview">
        <el-form-item prop="username">
          <el-input v-model="loginForm.username"
                    prefix-icon="el-icon-user"
                    placeholder="用户名称" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="loginForm.password"
                    prefix-icon="el-icon-lock"
                    type="password"
                    placeholder="用户密码" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary"
                     class="btn"
                     @click="login">登陆</el-button>
        </el-form-item>
      </el-form>

      <el-form ref="registerForm"
               :model="registerForm"
               :rules="registerRules"
               label-position="left"
               v-show="!lrview">
        <el-form-item prop="username">
          <el-input v-model="registerForm.username"
                    prefix-icon="el-icon-user"
                    placeholder="用户名称" />
        </el-form-item>
        <el-form-item prop="email">
          <el-input v-model="registerForm.email"
                    prefix-icon="el-icon-message"
                    placeholder="用户邮箱" />
        </el-form-item>
        <el-form-item prop="validatecode">
          <el-input v-model="registerForm.validatecode"
                    prefix-icon="el-icon-key"
                    placeholder="邮箱验证码" />
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="registerForm.password"
                    prefix-icon="el-icon-lock"
                    type="password"
                    placeholder="用户密码" />
        </el-form-item>
        <el-form-item class="btn2">
          <el-button type="primary"
                     @click="validateEmail">验证邮箱</el-button>
          <el-button type="primary"
                     @click="register">注册</el-button>
        </el-form-item>
      </el-form>
    </el-drawer>
  </el-row>
</template>

<script>
export default {
  props: {
    tabtitle: {
      type: Array,
      default: () => ['首页', '肿瘤', '罕见病', '关于']
    }
  },
  data () {
    return {
      currentIndex: 0,
      drawer: false,
      lr: ['登陆', '注册'],
      lrIndex: 0,
      lrview: true,
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [
          { required: true, message: '请输入用户名称', trigger: 'blur' },
          { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
        ]
      },
      registerForm: {
        username: '',
        email: '',
        validatecode: '',
        password: ''
      },
      registerRules: {
        username: [
          { required: true, message: '请输入用户名称', trigger: 'blur' },
          { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入用户邮箱', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        validatecode: [
          { required: true, message: '请输入邮箱验证码', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入用户密码', trigger: 'blur' },
          { min: 6, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.currentIndex = window.sessionStorage.getItem('idx')
  },
  methods: {
    closeDrawer () {
      this.$refs.loginForm.resetFields()
      this.$refs.registerForm.resetFields()
    },
    handle (i) {
      switch (i) {
        case 0:
          this.$router.push('/index').catch(err => err)
          break
        case 1:
          this.$router.push('/cancer').catch(err => err)
          break
        case 2:
          this.$router.push('/rare').catch(err => err)
          break
        case 3:
          this.$router.push('/about').catch(err => err)
      }
      this.currentIndex = i
      window.sessionStorage.setItem('idx', i)
    },
    clickLR (i) {
      if (this.lrIndex !== i) {
        this.lrIndex = i
        this.lrview = !this.lrview
      }
    },
    login () {
      this.$refs.loginForm.validate(async valid => {
        if (!valid) {
          return null
        }
        // const { data: res } = await this.$http.post('user/login', this.form)
        // if (res.status !== 200) return this.$message.error('密码或用户名称错误！')
        // this.$message.success('登陆成功！')
        // window.sessionStorage.setItem('token', res.token)
        // window.sessionStorage.setItem('name', res.name)
        // this.$router.push('/home')
      })
    },
    validateEmail () {
      if (this.registerForm.email) {
        this.$message.success(`已发送验证码到${this.registerForm.email}`)
      } else {
        this.$message.warning('用户邮箱不能为空')
      }
    },
    register () {
      this.$refs.registerForm.validate(async valid => {
        if (!valid) {
          return null
        }
      })
    }
  }
}
</script>

<style scoped>
/* background-color: #455A64; */
.el-row {
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-color: #455a64;
  color: #ffffff;
  width: 100vw;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1;
}
.title {
  text-align: center;
  font-size: 30px;
}
.rightbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
.rightbar div {
  cursor: pointer;
}
.el-button {
  border: #607d8b;
}
.el-button:hover {
  color: #ffffff;
  background-color: #607d8b;
  border: #607d8b;
}
.active {
  color: #009688;
}
.tabs {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  color: black;
}
.tabs div {
  cursor: pointer;
  border-bottom: 2px solid;
  padding: 0 10px 7px 10px;
}
.lractive {
  color: #009688;
  border-bottom-color: #009688;
}
.el-form {
  margin-top: 10%;
}
.el-form-item {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
.btn {
  width: 100%;
}
.btn2 {
  display: flex;
  justify-content: space-around;
}
</style>
