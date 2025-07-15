(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增地质数据",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增地质数据",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/geology_data/geology_data",
              "messages": {
                "success": "添加成功",
                "failed": "添加失败"
              }
            },
            "body": [
              {
                "type": "input-text",
                "name": "connect_key",
                "label": "盾构机编号",
                "required": true
              },
              {
                "type": "input-number",
                "name": "ring",
                "label": "对应环号",
                "required": true
              },
              {
                "type": "input-text",
                "name": "sub_code",
                "label": "施工区间编码",
                "required": true
              },
              {
                "type": "input-text",
                "name": "sub_name",
                "label": "施工区间名称",
                "required": true
              },
              {
                "type": "input-text",
                "name": "layer_name",
                "label": "地层名称"
              },
              {
                "type": "input-text",
                "name": "type",
                "label": "地层类型"
              },
              {
                "type": "input-text",
                "name": "soil_surface_params",
                "label": "土体（开挖面）参数"
              },
              {
                "type": "input-text",
                "name": "cover_thickness",
                "label": "覆盖层厚度"
              },
              {
                "type": "input-text",
                "name": "water_level",
                "label": "水位线高度"
              },
              {
                "type": "input-text",
                "name": "permeability",
                "label": "渗透系数"
              },
              {
                "type": "input-text",
                "name": "cohesion",
                "label": "粘聚力"
              },
              {
                "type": "input-text",
                "name": "internal_friction",
                "label": "内摩擦角"
              },
              {
                "type": "input-text",
                "name": "deformation_modulus",
                "label": "变形模量"
              },
              {
                "type": "input-text",
                "name": "poissons_ratio",
                "label": "泊松比"
              },
              {
                "type": "input-text",
                "name": "lateral_pressure",
                "label": "侧压力系数"
              },
              {
                "type": "input-text",
                "name": "overlying_soil_params",
                "label": "上覆土层参数"
              },
              {
                "type": "input-number",
                "name": "water_content",
                "label": "天然含水量"
              },
              {
                "type": "input-number",
                "name": "sol_specific_gravity",
                "label": "土粒比重"
              },
              {
                "type": "input-number",
                "name": "natural_porosity_ratio",
                "label": "孔隙比"
              },
              {
                "type": "input-number",
                "name": "liquid_limit",
                "label": "液限"
              },
              {
                "type": "input-number",
                "name": "plastic_limit",
                "label": "塑限"
              },
              {
                "type": "input-number",
                "name": "plasticity_index",
                "label": "塑性指数"
              },
              {
                "type": "input-number",
                "name": "liquidity_index",
                "label": "液性指数"
              },
              {
                "type": "input-number",
                "name": "compression_coefficient",
                "label": "压缩系数"
              },
              {
                "type": "input-number",
                "name": "compression_modulus",
                "label": "压缩模量"
              },
              {
                "type": "input-number",
                "name": "quick_shear_friction_angle",
                "label": "快剪摩擦角"
              },
              {
                "type": "input-number",
                "name": "quick_shear_cohesion",
                "label": "快剪粘聚力"
              },
              {
                "type": "input-number",
                "name": "consolidated_friction_angle",
                "label": "固结摩擦角"
              }
            ]
          }
        }
      },
      {
        "type": "crud",
        "syncLocation": false,
        "resizable": true,
        "columnsTogglable": true,
        "className": "table-db m-b-none",
        "tableClassName": "table-cell-nowrap",
        "api": {
          "url": "/geology_data/geology_data_list",
          "method": "get",
          "dataType": "json",
          "adaptor": function (payload) {
            return {
              status: payload.status,
              msg: payload.msg,
              data: {
                items: payload.data && payload.data.items ? payload.data.items : [],
                total: payload.data && payload.data.total ? payload.data.total : 0
              }
            };
          }
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-list'></i> 地质数据管理</div>"
          },
          "export-excel",
          {
            "type": "reload",
            "icon": "fa fa-refresh",
            "tooltip": "刷新数据",
            "tooltipPlacement": "top",
            "level": "link"
          }
        ],
        "filter": {
          "title": "查询条件",
          "submitText": "查询",
          "body": [
            {
              "type": "input-text",
              "name": "connect_key",
              "label": "盾构机编号",
              "placeholder": "请输入盾构机编号进行查询"
            },
            {
              "type": "input-text",
              "name": "sub_code",
              "label": "施工区间编码",
              "placeholder": "请输入施工区间编码进行查询"
            },
            {
              "type": "input-text",
              "name": "sub_name",
              "label": "施工区间名称",
              "placeholder": "请输入施工区间名称进行查询"
            }
          ]
        },
        "columns": [
          {
            "type": "operation",
            "label": "操作",
            "width": 80,
            "fixed": "right",
            "buttons": [
              {
                "type": "button",
                "icon": "fa fa-pencil",
                "tooltip": "修改",
                "level": "link",
                "actionType": "drawer",
                "drawer": {
                  "position": "right",
                  "size": "lg",
                  "title": "修改地质数据",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/geology_data/update_geology_data",
                      "messages": {
                        "success": "修改成功",
                        "failed": "修改失败"
                      }
                    },
                    "body": [
                      {
                        "type": "hidden",
                        "name": "id"
                      },
                      {
                        "type": "input-text",
                        "name": "connect_key",
                        "label": "盾构机编号",
                        "required": true
                      },
                      {
                        "type": "input-number",
                        "name": "ring",
                        "label": "对应环号",
                        "required": true
                      },
                      {
                        "type": "input-text",
                        "name": "sub_code",
                        "label": "施工区间编码",
                        "required": true
                      },
                      {
                        "type": "input-text",
                        "name": "sub_name",
                        "label": "施工区间名称",
                        "required": true
                      },
                      {
                        "type": "input-text",
                        "name": "layer_name",
                        "label": "地层名称"
                      },
                      {
                        "type": "input-text",
                        "name": "type",
                        "label": "地层类型"
                      },
                      {
                        "type": "input-text",
                        "name": "soil_surface_params",
                        "label": "土体（开挖面）参数"
                      },
                      {
                        "type": "input-text",
                        "name": "cover_thickness",
                        "label": "覆盖层厚度"
                      },
                      {
                        "type": "input-text",
                        "name": "water_level",
                        "label": "水位线高度"
                      },
                      {
                        "type": "input-text",
                        "name": "permeability",
                        "label": "渗透系数"
                      },
                      {
                        "type": "input-text",
                        "name": "cohesion",
                        "label": "粘聚力"
                      },
                      {
                        "type": "input-text",
                        "name": "internal_friction",
                        "label": "内摩擦角"
                      },
                      {
                        "type": "input-text",
                        "name": "deformation_modulus",
                        "label": "变形模量"
                      },
                      {
                        "type": "input-text",
                        "name": "poissons_ratio",
                        "label": "泊松比"
                      },
                      {
                        "type": "input-text",
                        "name": "lateral_pressure",
                        "label": "侧压力系数"
                      },
                      {
                        "type": "input-text",
                        "name": "overlying_soil_params",
                        "label": "上覆土层参数"
                      },
                      {
                        "type": "input-number",
                        "name": "water_content",
                        "label": "天然含水量"
                      },
                      {
                        "type": "input-number",
                        "name": "sol_specific_gravity",
                        "label": "土粒比重"
                      },
                      {
                        "type": "input-number",
                        "name": "natural_porosity_ratio",
                        "label": "孔隙比"
                      },
                      {
                        "type": "input-number",
                        "name": "liquid_limit",
                        "label": "液限"
                      },
                      {
                        "type": "input-number",
                        "name": "plastic_limit",
                        "label": "塑限"
                      },
                      {
                        "type": "input-number",
                        "name": "plasticity_index",
                        "label": "塑性指数"
                      },
                      {
                        "type": "input-number",
                        "name": "liquidity_index",
                        "label": "液性指数"
                      },
                      {
                        "type": "input-number",
                        "name": "compression_coefficient",
                        "label": "压缩系数"
                      },
                      {
                        "type": "input-number",
                        "name": "compression_modulus",
                        "label": "压缩模量"
                      },
                      {
                        "type": "input-number",
                        "name": "quick_shear_friction_angle",
                        "label": "快剪摩擦角"
                      },
                      {
                        "type": "input-number",
                        "name": "quick_shear_cohesion",
                        "label": "快剪粘聚力"
                      },
                      {
                        "type": "input-number",
                        "name": "consolidated_friction_angle",
                        "label": "固结摩擦角"
                      }
                    ]
                  }
                }
              },
              {
                "type": "button",
                "icon": "fa fa-times text-danger",
                "actionType": "ajax",
                "tooltip": "删除",
                "level": "link",
                "confirmText": "确认要删除？",
                "api": {
                  "method": "delete",
                  "url": "/geology_data/delete_geology_data/${id}"
                }
              }
            ]
          },
          {
            "name": "id",
            "label": "编号",
            "sortable": true
          },
          {
            "name": "connect_key",
            "label": "盾构机编号",
            "sortable": true
          },
          {
            "name": "ring",
            "label": "对应环号",
            "sortable": true
          },
          {
            "name": "sub_code",
            "label": "施工区间编码",
            "sortable": true
          },
          {
            "name": "sub_name",
            "label": "施工区间名称",
            "sortable": true
          },
          {
            "name": "layer_name",
            "label": "地层名称",
            "sortable": true
          },
          {
            "name": "type",
            "label": "地层类型",
            "sortable": true
          },
          {
            "name": "soil_surface_params",
            "label": "土体（开挖面）参数",
            "sortable": true
          },
          {
            "name": "cover_thickness",
            "label": "覆盖层厚度",
            "sortable": true
          },
          {
            "name": "water_level",
            "label": "水位线高度",
            "sortable": true
          },
          {
            "name": "permeability",
            "label": "渗透系数",
            "sortable": true
          },
          {
            "name": "cohesion",
            "label": "粘聚力",
            "sortable": true
          },
          {
            "name": "internal_friction",
            "label": "内摩擦角",
            "sortable": true
          },
          {
            "name": "deformation_modulus",
            "label": "变形模量",
            "sortable": true
          },
          {
            "name": "poissons_ratio",
            "label": "泊松比",
            "sortable": true
          },
          {
            "name": "lateral_pressure",
            "label": "侧压力系数",
            "sortable": true
          },
          {
            "name": "overlying_soil_params",
            "label": "上覆土层参数",
            "sortable": true
          },
          {
            "name": "water_content",
            "label": "天然含水量",
            "sortable": true
          },
          {
            "name": "sol_specific_gravity",
            "label": "土粒比重",
            "sortable": true
          },
          {
            "name": "natural_porosity_ratio",
            "label": "孔隙比",
            "sortable": true
          },
          {
            "name": "liquid_limit",
            "label": "液限",
            "sortable": true
          },
          {
            "name": "plastic_limit",
            "label": "塑限",
            "sortable": true
          },
          {
            "name": "plasticity_index",
            "label": "塑性指数",
            "sortable": true
          },
          {
            "name": "liquidity_index",
            "label": "液性指数",
            "sortable": true
          },
          {
            "name": "compression_coefficient",
            "label": "压缩系数",
            "sortable": true
          },
          {
            "name": "compression_modulus",
            "label": "压缩模量",
            "sortable": true
          },
          {
            "name": "quick_shear_friction_angle",
            "label": "快剪摩擦角",
            "sortable": true
          },
          {
            "name": "quick_shear_cohesion",
            "label": "快剪粘聚力",
            "sortable": true
          },
          {
            "name": "consolidated_friction_angle",
            "label": "固结摩擦角",
            "sortable": true
          }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();