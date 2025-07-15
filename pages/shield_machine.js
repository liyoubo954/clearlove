(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增盾构机信息",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增盾构机信息",
          "body": {
            "type": "form",
            "api": {
              "method": "post",
              "url": "/shield_machine/shield_machine",
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
                "label": "施工环号",
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
                "name": "digging_diameter",
                "label": "盾构机开挖直径"
              },
              {
                "type": "input-text",
                "name": "total_length",
                "label": "盾构机总长"
              },
              {
                "type": "input-text",
                "name": "total_weight",
                "label": "盾构机总重"
              },
              {
                "type": "input-text",
                "name": "design_pressure",
                "label": "盾构机设计压力"
              },
              {
                "type": "input-text",
                "name": "working_pressure",
                "label": "盾构机工作压力"
              },
              {
                "type": "input-text",
                "name": "max_thrust",
                "label": "盾构机最大推力"
              },
              {
                "type": "input-text",
                "name": "max_cutter_speed",
                "label": "盾构机最大刀盘转速"
              },
              {
                "type": "input-text",
                "name": "DP_XZNJ",
                "label": "刀盘旋转扭矩"
              },
              {
                "type": "input-text",
                "name": "DP_SDNJ",
                "label": "刀盘扭矩"
              },
              {
                "type": "input-text",
                "name": "DP_KKL",
                "label": "刀盘开口率"
              },
              {
                "type": "input-text",
                "name": "max_advance_speed",
                "label": "最大推进速度"
              },
              {
                "type": "input-text",
                "name": "cylinder_layout",
                "label": "油缸布置形式"
              },
              {
                "type": "input-text",
                "name": "shield_type",
                "label": "盾构机类型"
              },
              {
                "type": "input-text",
                "name": "construction_loc",
                "label": "项目施工位置"
              },
              {
                "type": "input-text",
                "name": "start_end_section",
                "label": "起始区间、走向等"
              },
              {
                "type": "input-text",
                "name": "ring_segment_size",
                "label": "每环尺寸"
              },
              {
                "type": "input-text",
                "name": "tail_brush_count",
                "label": "盾尾刷道数"
              },
              {
                "type": "input-text",
                "name": "tail_gap",
                "label": "盾尾间隙"
              },
              {
                "type": "input-text",
                "name": "grease_pressure",
                "label": "油脂压力"
              },
              {
                "type": "input-text",
                "name": "yzcs",
                "label": "油脂参数"
              },
              {
                "type": "input-text",
                "name": "gd_cc",
                "label": "管道尺寸"
              },
              {
                "type": "input-text",
                "name": "gd_sl",
                "label": "管道数量"
              },
              {
                "type": "input-text",
                "name": "jy_ls",
                "label": "浆液流量"
              },
              {
                "type": "input-text",
                "name": "jy_nd",
                "label": "浆液浓度"
              },
              {
                "type": "input-text",
                "name": "cz_ll",
                "label": "出渣粒径"
              },
              {
                "type": "input-text",
                "name": "jb_psxs",
                "label": "搅拌破碎形式"
              },
              {
                "type": "input-text",
                "name": "flushing_nozzle_quantity",
                "label": "冲洗喷嘴数量"
              },
              {
                "type": "input-text",
                "name": "flushing_nozzle_type",
                "label": "冲洗喷嘴形式"
              },
              {
                "type": "input-text",
                "name": "flushing_flow",
                "label": "冲洗流量"
              },
              {
                "type": "input-text",
                "name": "property_unit",
                "label": "产权单位"
              },
              {
                "type": "input-text",
                "name": "project_status",
                "label": "项目状态"
              },
              {
                "type": "input-text",
                "name": "equipment_property",
                "label": "设备性质"
              },
              {
                "type": "input-text",
                "name": "equipment_brand",
                "label": "设备品牌"
              },
              {
                "type": "input-text",
                "name": "segment_outside_diameter",
                "label": "管片外径"
              },
              {
                "type": "input-text",
                "name": "segment_width",
                "label": "管片宽度"
              },
              {
                "type": "input-text",
                "name": "manufacturer",
                "label": "生产厂家"
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
          "url": "/shield_machine/shield_machine_list",
          "method": "get",
          "dataType": "json"
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 盾构机基本信息管理</div>"
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
              "type": "input-number",
              "name": "ring",
              "label": "施工环号",
              "placeholder": "请输入施工环号进行查询"
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
                  "title": "修改盾构机信息",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/shield_machine/update_shield_machine",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "connect_key", "label": "盾构机编号", "required": true},
                      {"type": "input-number", "name": "ring", "label": "施工环号", "required": true},
                      {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "required": true},
                      {"type": "input-number", "name": "project_stats_id", "label": "项目统计ID", "required": false},
                      {"type": "input-text", "name": "digging_diameter", "label": "盾构机开挖直径"},
                      {"type": "input-text", "name": "total_length", "label": "盾构机总长"},
                      {"type": "input-text", "name": "total_weight", "label": "盾构机总重"},
                      {"type": "input-text", "name": "design_pressure", "label": "盾构机设计压力"},
                      {"type": "input-text", "name": "working_pressure", "label": "盾构机工作压力"},
                      {"type": "input-text", "name": "max_thrust", "label": "盾构机最大推力"},
                      {"type": "input-text", "name": "max_cutter_speed", "label": "盾构机最大刀盘转速"},
                      {"type": "input-text", "name": "DP_XZNJ", "label": "刀盘旋转扭矩"},
                      {"type": "input-text", "name": "DP_SDNJ", "label": "刀盘扭矩"},
                      {"type": "input-text", "name": "DP_KKL", "label": "刀盘开口率"},
                      {"type": "input-text", "name": "max_advance_speed", "label": "最大推进速度"},
                      {"type": "input-text", "name": "cylinder_layout", "label": "油缸布置形式"},
                      {"type": "input-text", "name": "shield_type", "label": "盾构机类型"},
                      {"type": "input-text", "name": "construction_loc", "label": "项目施工位置"},
                      {"type": "input-text", "name": "start_end_section", "label": "起始区间、走向等"},
                      {"type": "input-text", "name": "ring_segment_size", "label": "每环尺寸"},
                      {"type": "input-text", "name": "tail_brush_count", "label": "盾尾刷道数"},
                      {"type": "input-text", "name": "tail_gap", "label": "盾尾间隙"},
                      {"type": "input-text", "name": "grease_pressure", "label": "油脂压力"},
                      {"type": "input-text", "name": "yzcs", "label": "油脂参数"},
                      {"type": "input-text", "name": "gd_cc", "label": "管道尺寸"},
                      {"type": "input-text", "name": "gd_sl", "label": "管道数量"},
                      {"type": "input-text", "name": "jy_ls", "label": "浆液流量"},
                      {"type": "input-text", "name": "jy_nd", "label": "浆液浓度"},
                      {"type": "input-text", "name": "cz_ll", "label": "出渣粒径"},
                      {"type": "input-text", "name": "jb_psxs", "label": "搅拌破碎形式"},
                      {"type": "input-text", "name": "flushing_nozzle_quantity", "label": "冲洗喷嘴数量"},
                      {"type": "input-text", "name": "flushing_nozzle_type", "label": "冲洗喷嘴形式"},
                      {"type": "input-text", "name": "flushing_flow", "label": "冲洗流量"},
                      {"type": "input-text", "name": "property_unit", "label": "产权单位"},
                      {"type": "input-text", "name": "project_status", "label": "项目状态"},
                      {"type": "input-text", "name": "equipment_property", "label": "设备性质"},
                      {"type": "input-text", "name": "equipment_brand", "label": "设备品牌"},
                      {"type": "input-text", "name": "segment_outside_diameter", "label": "管片外径"},
                      {"type": "input-text", "name": "segment_width", "label": "管片宽度"},
                      {"type": "input-text", "name": "manufacturer", "label": "生产厂家"}
                    ]
                  }
                }
              },
              {
                "type": "button",
                "icon": "fa fa-times text-danger",
                "actionType": "ajax",
                "tooltip": "删除",
                "confirmText": "确定要删除该记录吗？",
                "api": {
                  "method": "delete",
                  "url": "/shield_machine/delete_shield_machine/${id}"
                },
                "messages": {
                  "success": "删除成功",
                  "failed": "删除失败"
                }
              }
            ]
          },
          { "name": "id", "label": "编号", "type": "number", "width": 80 },
          { "name": "connect_key", "label": "盾构机编号", "type": "text", "width": 120 },
          { "name": "ring", "label": "施工环号", "type": "number", "width": 100 },
          { "name": "sub_code", "label": "施工区间编码", "type": "text", "width": 120 },
          { "name": "sub_name", "label": "施工区间名称", "type": "text", "width": 150 },
          { "name": "digging_diameter", "label": "盾构机开挖直径", "type": "text", "width": 120 },
          { "name": "total_length", "label": "盾构机总长", "type": "text", "width": 120 },
          { "name": "total_weight", "label": "盾构机总重", "type": "text", "width": 120 },
          { "name": "design_pressure", "label": "盾构机设计压力", "type": "text", "width": 150 },
          { "name": "working_pressure", "label": "盾构机工作压力", "type": "text", "width": 150 },
          { "name": "max_thrust", "label": "盾构机最大推力", "type": "text", "width": 150 },
          { "name": "max_cutter_speed", "label": "盾构机最大刀盘转速", "type": "text", "width": 150 },
          { "name": "DP_XZNJ", "label": "刀盘旋转扭矩", "type": "text", "width": 120 },
          { "name": "DP_SDNJ", "label": "刀盘扭矩", "type": "text", "width": 120 },
          { "name": "DP_KKL", "label": "刀盘开口率", "type": "text", "width": 120 },
          { "name": "max_advance_speed", "label": "最大推进速度", "type": "text", "width": 120 },
          { "name": "cylinder_layout", "label": "油缸布置形式", "type": "text", "width": 120 },
          { "name": "shield_type", "label": "盾构机类型", "type": "text", "width": 120 },
          { "name": "construction_loc", "label": "项目施工位置", "type": "text", "width": 150 },
          { "name": "start_end_section", "label": "起始区间、走向等", "type": "text", "width": 150 },
          { "name": "ring_segment_size", "label": "每环尺寸", "type": "text", "width": 120 },
          { "name": "tail_brush_count", "label": "盾尾刷道数", "type": "text", "width": 120 },
          { "name": "tail_gap", "label": "盾尾间隙", "type": "text", "width": 120 },
          { "name": "grease_pressure", "label": "油脂压力", "type": "text", "width": 120 },
          { "name": "yzcs", "label": "油脂参数", "type": "text", "width": 120 },
          { "name": "gd_cc", "label": "管道尺寸", "type": "text", "width": 120 },
          { "name": "gd_sl", "label": "管道数量", "type": "text", "width": 120 },
          { "name": "jy_ls", "label": "浆液流量", "type": "text", "width": 120 },
          { "name": "jy_nd", "label": "浆液浓度", "type": "text", "width": 120 },
          { "name": "cz_ll", "label": "出渣粒径", "type": "text", "width": 120 },
          { "name": "jb_psxs", "label": "搅拌破碎形式", "type": "text", "width": 150 },
          { "name": "flushing_nozzle_quantity", "label": "冲洗喷嘴数量", "type": "text", "width": 150 },
          { "name": "flushing_nozzle_type", "label": "冲洗喷嘴形式", "type": "text", "width": 150 },
          { "name": "flushing_flow", "label": "冲洗流量", "type": "text", "width": 120 },
          { "name": "property_unit", "label": "产权单位", "type": "text", "width": 120 },
          { "name": "project_status", "label": "项目状态", "type": "text", "width": 120 },
          { "name": "equipment_property", "label": "设备性质", "type": "text", "width": 120 },
          { "name": "equipment_brand", "label": "设备品牌", "type": "text", "width": 120 },
          { "name": "segment_outside_diameter", "label": "管片外径", "type": "text", "width": 120 },
          { "name": "segment_width", "label": "管片宽度", "type": "text", "width": 120 },
          { "name": "manufacturer", "label": "生产厂家", "type": "text", "width": 120 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();