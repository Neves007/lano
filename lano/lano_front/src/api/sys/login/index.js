import request from '@/plugin/axios'

let base_url = 'http://127.0.0.1:8000/';

export function AccountLogin (data) {
  console.log("login/index  AccountLogin函数执行")
  return request({
    url: base_url + 'api/login',
    method: 'post',
    data
  })
}