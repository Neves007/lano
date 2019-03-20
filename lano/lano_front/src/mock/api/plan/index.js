import Mock from 'mockjs'
let Random = Mock.Random

let plan_name = ['四川大学全网监测方案','成都高校敏感监测方案','山西高校校园贷监测方案','太原教育督导监测方案',
    '武侯区幼儿园敏感监测方案','锦江区中小学监测方案']
let plan_list = [

    {
        id :Random.increment(),
        name: '太原市迎泽区教育舆情监测方案',
        region: Random.county(true),
        person:Random.cname(),
        thing:'教育督导',
        except:'娱乐',
    },
    {
        id :Random.increment(),
        name: Random.pick(plan_name),
        region: Random.county(true),
        person:Random.cname(),
        thing:'教育督导',
        except:'娱乐',
    },
    {
        id :Random.increment(),
        name: Random.pick(plan_name),
        region: Random.county(true),
        person:Random.cname(),
        thing:'教育督导',
        except:'娱乐',
    },
    {
        id :Random.increment(),
        name: Random.pick(plan_name),
        region: Random.county(true),
        person:Random.cname(),
        thing:'教育督导',
        except:'娱乐',
    },
]

Mock.mock('/api/plan/plan_list', 'get', () => {
    return {
        code: 0,
        plan: plan_list
    }
})

Mock.mock('/api/plan/plan_add', 'post', (options) => {
    console.log('options %o', options)

    let newplan = JSON.parse(options.body)
    newplan['id'] = Random.increment()

    plan_list.push(newplan)

    return {
        code: 0,
        plan: plan_list
    }
})


