import request from '@/plugin/axios'

let base_url = 'http://127.0.0.1:8000/api/';

export function GetInfolist(){
    return request({
        url:base_url+'get_infolist',
        method:'get',
        data
    })
}