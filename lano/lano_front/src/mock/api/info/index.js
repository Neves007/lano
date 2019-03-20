import Mock from 'mockjs'
let Random = Mock.Random

let source = ['新浪微博', '微信公众号', '新闻门户', '贴吧', '论坛']
let tag = ['高考', '商学院', '少儿英语', '考研', '公务员', '四六级', '出国']

let info_list = [
  {
    'id': Random.id(),
    'username': Random.name(),
    'content': Random.cparagraph(5, 10),
    'is_checked': false,
    'sensitive_state': Random.boolean(5, 5, true),
    'article_source': Random.boolean(3, 1, true),
    'article_province': Random.province(),
    'same_article': Random.natural(1, 30),
    'source|1': source,
    'tag|1': tag,
    'is_read': false,
      'feelings|1': ['1','2','3'],
      'warning_level|1':['1', '2', '3']
  },
  {
    id: Random.id(),
    username: Random.cname(),
    content: Random.cparagraph(5, 10),
    is_checked: false,
    sensitive_state: Random.boolean(5, 5, true),
    article_source: Random.boolean(3, 1, true),
    article_province: Random.province(),
    same_article: Random.natural(1, 30),
    'source|1': source,
    'tag|1': tag,
    is_read: false,
      'feelings|1': ['1','2','3'],
      'warning_level|1':['1', '2', '3']
  },
  {
    id: Random.id(),
    username: Random.name(),
    content: Random.cparagraph(5, 10),
    is_checked: false,
    sensitive_state: Random.boolean(5, 5, true),
    article_source: Random.boolean(3, 1, true),
    article_province: Random.province(),
    same_article: Random.natural(1, 30),
    'source|1': source,
    'tag|1': tag,
    is_read: false,
      'feelings|1': ['1','2','3'],
      'warning_level|1':['1', '2', '3']
  },
  {
    id: Random.id(),
    username: Random.cname(),
    content: Random.cparagraph(5, 10),
    is_checked: false,
    sensitive_state: Random.boolean(5, 5, true),
    article_source: Random.boolean(3, 1, true),
    article_province: Random.province(),
    same_article: Random.natural(1, 30),
    'source|1': source,
    'tag|1': tag,
    is_read: false,
      'feelings|1': ['1','2','3'],
      'warning_level|1':['1', '2', '3']
  },
]

Mock.mock('/api/info/info_list', 'get', () => {
  return {
    code: 0,
    info_list: Mock.mock(info_list)
  }
})

Mock.mock('/api/info/sensitive_change', 'post', (options) => {
  let idobj = JSON.parse(options.body)
  let info = info_list.find(e => e.id === idobj.id)
  let index = info_list.indexOf(info)

  info_list[index]['sensitive_state'] = !info_list[index]['sensitive_state']

  return {
    code: 0,
    // info_list: Mock.mock(info_list)
  }
})

Mock.mock('/api/info/choose_change', 'post', (options) => {
  let idobj = JSON.parse(options.body)
  let info = info_list.find(e => e.id === idobj.id)
  let index = info_list.indexOf(info)
  info_list[index]['is_checked'] = !info_list[index]['is_checked']
  return {
    code: 0,
  }
})
Mock.mock('/api/info/readstate_change', 'post', (options) => {
  let idobj = JSON.parse(options.body)
  let info = info_list.find(e => e.id === idobj.id)
  let index = info_list.indexOf(info)
  info_list[index]['is_read'] = !info_list[index]['is_read']
  return {
    code: 0,
  }
})
