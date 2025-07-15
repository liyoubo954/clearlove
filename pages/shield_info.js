(function () {
  const response = {
    "type": "page",
    "body": [
      {
        "type": "button",
        "label": "新增掘进参数",
        "icon": "fa fa-plus",
        "level": "primary",
        "className": "m-b-sm",
        "actionType": "dialog",
        "dialog": {
          "title": "新增掘进参数",
          "body": {
            "type": "form",
            "api": {
            "method": "post",
            "url": "/shield_info/shield_info",
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
                "label": "施工环号"
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
                "name": "record_time",
                "label": "记录时间"
              },
              {
                "type": "input-text",
                "name": "device_roll",
                "label": "设备侧滚"
              },
              {
                "type": "input-text",
                "name": "device_pitch",
                "label": "设备倾角"
              },
              {
                "type": "input-text",
                "name": "main_drive_speed",
                "label": "主驱动转速"
              },
              {
                "type": "input-text",
                "name": "main_drive_torque",
                "label": "主驱动扭矩"
              },
              {
                "type": "input-text",
                "name": "main_drive_temp",
                "label": "主驱动温度"
              },
              {
                "type": "input-text",
                "name": "main_drive_current",
                "label": "主驱动电流"
              },
              {
                "type": "input-text",
                "name": "main_drive_grease",
                "label": "主驱动密封油脂量"
              },
              {
                "type": "input-text",
                "name": "kwc_prs",
                "label": "开挖仓压力"
              },
              {
                "type": "input-text",
                "name": "gzc_prs",
                "label": "工作仓压力"
              },
              {
                "type": "input-text",
                "name": "tjyg_prs",
                "label": "推进油缸压力"
              },
              {
                "type": "input-text",
                "name": "ztl",
                "label": "总推力"
              },
              {
                "type": "input-text",
                "name": "fqyg_prs",
                "label": "分区油缸压力"
              },
              {
                "type": "input-text",
                "name": "yg_tl",
                "label": "油缸推力"
              },
              {
                "type": "input-text",
                "name": "yggz_prs",
                "label": "油缸工作压力"
              },
              {
                "type": "input-text",
                "name": "yg_xc",
                "label": "油缸行程"
              },
              {
                "type": "input-text",
                "name": "jj_prs",
                "label": "进浆压力"
              },
              {
                "type": "input-text",
                "name": "cj_prs",
                "label": "出浆压力"
              },
              {
                "type": "input-text",
                "name": "nj_md",
                "label": "泥浆密度"
              },
              {
                "type": "input-text",
                "name": "nj_nd",
                "label": "泥浆粘度"
              },
              {
                "type": "input-text",
                "name": "nj_jflow",
                "label": "进浆流量"
              },
              {
                "type": "input-text",
                "name": "lxj_nj",
                "label": "螺旋机扭矩"
              },
              {
                "type": "input-text",
                "name": "lxj_prs",
                "label": "螺旋机压力"
              },
              {
                "type": "input-text",
                "name": "zj_prs",
                "label": "注浆压力"
              },
              {
                "type": "input-text",
                "name": "zjl",
                "label": "注浆量"
              },
              {
                "type": "input-text",
                "name": "jy_lx",
                "label": "浆液类型"
              },
              {
                "type": "input-text",
                "name": "yzzr_prs",
                "label": "油脂注入压力"
              },
              {
                "type": "input-text",
                "name": "main_drive_tail_seal_grease",
                "label": "主驱动盾尾密封油脂消耗量"
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
          "url": "/shield_info/shield_info_list",
          "method": "get",
          "dataType": "json"
        },
        "headerToolbar": [
          {
            "type": "tpl",
            "tpl": "<div class='header-title'><i class='fa fa-cog'></i> 掘进参数管理</div>"
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
                  "size": "md",
                  "title": "修改掘进参数",
                  "body": {
                    "type": "form",
                    "api": {
                      "method": "post",
                      "url": "/shield_info/update_shield_info",
                      "messages": {
                        "success": "更新成功",
                        "failed": "更新失败"
                      }
                    },
                    "body": [
                      {"type": "hidden", "name": "id"},
                      {"type": "input-text", "name": "connect_key", "label": "盾构机编号", "required": true},
                      {"type": "input-number", "name": "ring", "label": "施工环号"},
                      {"type": "input-text", "name": "sub_code", "label": "施工区间编码", "required": true},
                      {"type": "input-text", "name": "sub_name", "label": "施工区间名称", "required": true},
                      {"type": "input-text", "name": "record_time", "label": "记录时间"},
                      {"type": "input-text", "name": "device_roll", "label": "设备侧滚"},
                      {"type": "input-text", "name": "device_pitch", "label": "设备倾角"},
                      {"type": "input-text", "name": "main_drive_speed", "label": "主驱动转速"},
                      {"type": "input-text", "name": "main_drive_torque", "label": "主驱动扭矩"},
                      {"type": "input-text", "name": "main_drive_temp", "label": "主驱动温度"},
                      {"type": "input-text", "name": "main_drive_current", "label": "主驱动电流"},
                      {"type": "input-text", "name": "main_drive_grease", "label": "主驱动密封油脂量"},
                      {"type": "input-text", "name": "kwc_prs", "label": "开挖仓压力"},
                      {"type": "input-text", "name": "gzc_prs", "label": "工作仓压力"},
                      {"type": "input-text", "name": "tjyg_prs", "label": "推进油缸压力"},
                      {"type": "input-text", "name": "ztl", "label": "总推力"},
                      {"type": "input-text", "name": "fqyg_prs", "label": "分区油缸压力"},
                      {"type": "input-text", "name": "yg_tl", "label": "油缸推力"},
                      {"type": "input-text", "name": "yggz_prs", "label": "油缸工作压力"},
                      {"type": "input-text", "name": "yg_xc", "label": "油缸行程"},
                      {"type": "input-text", "name": "jj_prs", "label": "进浆压力"},
                      {"type": "input-text", "name": "cj_prs", "label": "出浆压力"},
                      {"type": "input-text", "name": "nj_md", "label": "泥浆密度"},
                      {"type": "input-text", "name": "nj_nd", "label": "泥浆粘度"},
                      {"type": "input-text", "name": "nj_jflow", "label": "进浆流量"},
                      {"type": "input-text", "name": "lxj_nj", "label": "螺旋机扭矩"},
                      {"type": "input-text", "name": "lxj_prs", "label": "螺旋机压力"},
                      {"type": "input-text", "name": "zj_prs", "label": "注浆压力"},
                      {"type": "input-text", "name": "zjl", "label": "注浆量"},
                      {"type": "input-text", "name": "jy_lx", "label": "浆液类型"},
                      {"type": "input-text", "name": "yzzr_prs", "label": "油脂注入压力"},
                      {"type": "input-text", "name": "main_drive_tail_seal_grease", "label": "主驱动盾尾密封油脂消耗量"}
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
                  "url": "/shield_info/delete_shield_info/${id}"
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
          { "name": "record_time", "label": "记录时间", "type": "text", "width": 150 },
          { "name": "device_roll", "label": "设备侧滚", "type": "text", "width": 100 },
          { "name": "device_pitch", "label": "设备倾角", "type": "text", "width": 100 },
          { "name": "main_drive_speed", "label": "主驱动转速", "type": "text", "width": 100 },
          { "name": "main_drive_torque", "label": "主驱动扭矩", "type": "text", "width": 100 },
          { "name": "main_drive_temp", "label": "主驱动温度", "type": "text", "width": 100 },
          { "name": "main_drive_current", "label": "主驱动电流", "type": "text", "width": 100 },
          { "name": "main_drive_grease", "label": "主驱动密封油脂量", "type": "text", "width": 150 },
          { "name": "kwc_prs", "label": "开挖仓压力", "type": "text", "width": 100 },
          { "name": "gzc_prs", "label": "工作仓压力", "type": "text", "width": 100 },
          { "name": "tjyg_prs", "label": "推进油缸压力", "type": "text", "width": 120 },
          { "name": "ztl", "label": "总推力", "type": "text", "width": 100 },
          { "name": "fqyg_prs", "label": "分区油缸压力", "type": "text", "width": 120 },
          { "name": "yg_tl", "label": "油缸推力", "type": "text", "width": 100 },
          { "name": "yggz_prs", "label": "油缸工作压力", "type": "text", "width": 120 },
          { "name": "yg_xc", "label": "油缸行程", "type": "text", "width": 100 },
          { "name": "jj_prs", "label": "进浆压力", "type": "text", "width": 100 },
          { "name": "cj_prs", "label": "出浆压力", "type": "text", "width": 100 },
          { "name": "nj_md", "label": "泥浆密度", "type": "text", "width": 100 },
          { "name": "nj_nd", "label": "泥浆粘度", "type": "text", "width": 100 },
          { "name": "nj_jflow", "label": "进浆流量", "type": "text", "width": 100 },
          { "name": "lxj_nj", "label": "螺旋机扭矩", "type": "text", "width": 120 },
          { "name": "lxj_prs", "label": "螺旋机压力", "type": "text", "width": 120 },
          { "name": "zj_prs", "label": "注浆压力", "type": "text", "width": 100 },
          { "name": "zjl", "label": "注浆量", "type": "text", "width": 100 },
          { "name": "jy_lx", "label": "浆液类型", "type": "text", "width": 100 },
          { "name": "yzzr_prs", "label": "油脂注入压力", "type": "text", "width": 120 },
          { "name": "main_drive_tail_seal_grease", "label": "主驱动盾尾密封油脂消耗量", "type": "text", "width": 200 }
        ]
      }
    ]
  };

  window.jsonpCallback && window.jsonpCallback(response);
})();