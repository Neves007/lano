import request from '@/plugin/axios'
let base_url = 'http://127.0.0.1:8000/';

export function AccountLogin (data) {
  return request({
    url: base_url + 'api/login',
    method: 'post',
    data
  })
}