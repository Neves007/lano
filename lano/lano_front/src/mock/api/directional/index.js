import Mock from 'mockjs'
let Random = Mock.Random


let weibo_name = ['教育大课堂','Susie的MTI课堂','新东方王江涛','英语老师Justin','肖秀荣教授','雅思口语','建昆老师']
let tieba_name = ['教育吧','山西招生考试网吧','山东教育厅吧','四川教育吧','江苏教育厅吧','计算机教育吧','海南考试局吧','绵阳高新区实验中学']
let website_name = ['新浪教育','网易新闻','中国青年网','澎湃新闻','凤凰网','人民日报','大公网','央视新闻','新华网']
let wechat_name = ['广东教育','浙江省教育工会','中青网教育','四川教育发布','宝安教育','福建教育微言','最美教育人','山西教育杂志','山西教育咨询中心']
let dir_website_tabledata = [
  {
      name: Random.pick(website_name),
      domain: Random.url(),
      status: Random.boolean(5, 5, true)
  },
  {
      name: Random.pick(website_name),
      domain: Random.url(),
      status: Random.boolean(5, 5, true)
  },
  {
      name: Random.pick(website_name),
      domain: Random.url(),
      status: Random.boolean(5, 5, true)
  }
]

let dir_weibo_tabledata = [
    {
        name: '微博昵称#' +Random.pick(weibo_name),
        uid: '微博id#' + Random.id(),
        status: Random.boolean(1, 9, true)
    },
    {
        name: '微博昵称#' +Random.pick(weibo_name),
        uid: '微博id#' + Random.id(),
        status: Random.boolean(8, 2, true)
    },
    {
        name: '微博昵称#' +Random.pick(weibo_name),
        uid: '微博id#' + Random.id(),
        status: Random.boolean(4, 6, true)
    }
]

let dir_wechat_tabledata = [
    {
        name: '公众号名称#' + Random.pick(wechat_name),
        wxid: '微信号#' + Random.id(),
        status: Random.boolean(1, 9, true)
    },
    {
        name: '公众号名称#' + Random.pick(wechat_name),
        wxid: '微信号#' + Random.id(),
        status: Random.boolean(1, 9, true)
    },
    {
        name: '公众号名称#' + Random.pick(wechat_name),
        wxid: '微信号#' + Random.id(),
        status: Random.boolean(1, 9, true)
    }
]

let dir_tieba_tabledata = [
    {
        name: Random.pick(tieba_name),
        introduction: Random.paragraph(1, 2),
        status: Random.boolean(1, 9, true)
    },
    {
        name: Random.pick(tieba_name),
        introduction:  Random.paragraph(1, 2),
        status: Random.boolean(5, 5, true)
    },
    {
        name: Random.pick(tieba_name),
        introduction:  Random.paragraph(1, 2),
        status: Random.boolean(8, 2, true)
    }
]
//website_list
Mock.mock('/api/directional/domain_list', 'get', () => {
  return {
    code: 0,
    domain: dir_website_tabledata
  }
})

Mock.mock('/api/directional/domain_add', 'post', (options) => {
    console.log(options)
  let domain = JSON.parse(options.body)
  domain['status'] = Random.boolean(5, 5, true)

  dir_website_tabledata.push(domain)

  return {
    code: 0,
    domain: dir_website_tabledata
  }
})

Mock.mock('/api/directional/domain_delete', 'post', (options) => {
    console.log(options)
    let index = JSON.parse(options.body)
    dir_website_tabledata.splice(index['index'],1)
    return {
        code: 0,
        domain: dir_website_tabledata
    }
})

//weibo_list
Mock.mock('/api/directional/weibo_list', 'get', () => {
    return {
        code: 0,
        weibo: dir_weibo_tabledata
    }
})

Mock.mock('/api/directional/weibo_add', 'post', (options) => {
    console.log(options)
    let weibo = JSON.parse(options.body)
    weibo['uid'] = '微博id#'+Random.id()
    weibo['status'] = Random.boolean(5, 5, true)

    dir_weibo_tabledata.push(weibo)

    return {
        code: 0,
        weibo: dir_weibo_tabledata
    }
})

Mock.mock('/api/directional/weibo_delete', 'post', (options) => {
    console.log(options)
    let index = JSON.parse(options.body)
    dir_weibo_tabledata.splice(index['index'],1)
    return {
        code: 0,
        weibo: dir_weibo_tabledata
    }
})

//wechat_list
Mock.mock('/api/directional/wechat_list', 'get', () => {
    return {
        code: 0,
        wechat: dir_wechat_tabledata
    }
})

Mock.mock('/api/directional/wechat_add', 'post', (options) => {
    console.log(options)
    let wechat = JSON.parse(options.body)
    wechat['wxid'] = '微信号#' + Random.id()
    wechat['status'] = Random.boolean(5, 5, true)

    dir_wechat_tabledata.push(wechat)

    return {
        code: 0,
        wechat: dir_wechat_tabledata
    }
})

Mock.mock('/api/directional/wechat_delete', 'post', (options) => {
    console.log(options)
    let index = JSON.parse(options.body)
    dir_wechat_tabledata.splice(index['index'],1)
    return {
        code: 0,
        wechat: dir_wechat_tabledata
    }
})

//tieba_list
Mock.mock('/api/directional/tieba_list', 'get', () => {
    return {
        code: 0,
        tieba: dir_tieba_tabledata
    }
})

Mock.mock('/api/directional/tieba_add', 'post', (options) => {
    console.log(options)
    let tieba = JSON.parse(options.body)
    tieba['introduction'] = Random.paragraph(1, 2)
    tieba['status'] = Random.boolean(5, 5, true)

    dir_tieba_tabledata.push(tieba)

    return {
        code: 0,
        tieba: dir_tieba_tabledata
    }
})

Mock.mock('/api/directional/tieba_delete', 'post', (options) => {
    console.log(options)
    let index = JSON.parse(options.body)
    dir_tieba_tabledata.splice(index['index'],1)
    return {
        code: 0,
        tieba: dir_tieba_tabledata
    }
})
