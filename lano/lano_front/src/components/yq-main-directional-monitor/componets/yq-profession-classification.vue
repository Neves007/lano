<template>
    <div>
        <el-row class="cu_domain_row">
            <el-checkbox class="domain_checkAll_box"
                         :indeterminate="directional_data.isIndeterminate"
                         v-model="directional_data.domain_checkAll"
                         @change="directional_domain_handleCheckAllChange" border
                         style="position: absolute; margin-left:52px;margin-top: 45px;">全选
            </el-checkbox>

            <el-checkbox-group class="domain_checkbox"
                               v-model="directional_data.domain_checked"
                               @change="directional_domain_handleCheckedCitiesChange">

                <el-checkbox v-for="domain in directional_data.domainOptions"
                             :label="domain" :key="domain" border>{{domain}}
                </el-checkbox>
            </el-checkbox-group>
        </el-row>
    </div>
</template>

<script>

    const directional_domain_Options = ['体制改革', '教育政策', '学校管理', '学科专业', '人才培养','招生',  '就业',
        '教师发展', '科学研究', '质量评估','社会服务','校园安全', '思想政治教育','教育反腐', '国外教育']
    export default {
        name: "yq-profession-classification",
        data() {
            return{
                directional_data: {
                    domain_checkAll: false,
                    domain_checked: ['教育反腐'],
                    domainOptions: directional_domain_Options,
                    isIndeterminate: true
            }

            }
        },
        methods:{
            directional_domain_handleCheckAllChange(val) {
                this.directional_data.domain_checked = val ? directional_domain_Options : []
                this.directional_data.isIndeterminate = false
            },
            directional_domain_handleCheckedCitiesChange(value) {
                let checkedCount = value.length
                this.directional_data.domain_checkAll = checkedCount === this.directional_data.domainOptions.length
                this.directional_data.isIndeterminate = checkedCount > 0 && checkedCount < this.directional_data.domainOptions.length
            }
        }
    }
</script>

<style scoped>

</style>