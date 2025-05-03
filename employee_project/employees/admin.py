from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group, Permission
from .models import Department, Employee, UserProfile
from django.db.models import Q

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'get_role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    
    def get_role(self, obj):
        return obj.profile.role if hasattr(obj, 'profile') else 'No role'
    get_role.short_description = 'Role'
    
    def save_model(self, request, obj, form, change):
        if not change:  # New user
            obj.set_password(form.cleaned_data['password1'])
            obj.is_staff = True  # 所有角色用户都是staff
            obj.is_active = True  # 默认激活
        super().save_model(request, obj, form, change)
    
    def save_formset(self, request, form, formset, change):
        # 确保组权限已设置
        self.ensure_group_permissions()
        
        instances = formset.save(commit=False)
        for instance in instances:
            if isinstance(instance, UserProfile):
                # 根据角色设置权限
                if instance.role == 'admin':
                    instance.user.is_superuser = True
                    instance.user.is_staff = True
                elif instance.role == 'hr':
                    instance.user.is_staff = True
                    # 获取HR组
                    hr_group = Group.objects.get(name='HR')
                    # 清除所有现有组
                    instance.user.groups.clear()
                    # 添加到HR组
                    instance.user.groups.add(hr_group)
                elif instance.role == 'employee':
                    instance.user.is_staff = True
                    # 获取Employee组
                    employee_group = Group.objects.get(name='Employee')
                    # 清除所有现有组
                    instance.user.groups.clear()
                    # 添加到Employee组
                    instance.user.groups.add(employee_group)
                
                instance.user.save()
        formset.save()
    
    def ensure_group_permissions(self):
        """确保所有组和权限已正确设置"""
        # HR组权限
        hr_group, created = Group.objects.get_or_create(name='HR')
        # 重置现有权限
        hr_group.permissions.clear()
        
        # HR权限codename列表
        hr_permission_codenames = [
            # 员工管理权限
            'add_employee', 'change_employee', 'view_employee',
            'add_userprofile', 'change_userprofile', 'view_userprofile',
            'add_department', 'change_department', 'view_department',
            # 考勤管理权限
            'add_attendance', 'change_attendance', 'view_attendance',
            # 绩效管理权限
            'add_performance', 'change_performance', 'view_performance',
            # 用户管理权限
            'view_user',
        ]
        
        # 获取所有存在的权限
        existing_hr_permissions = Permission.objects.filter(
            Q(codename__in=hr_permission_codenames)
        )
        # 设置HR组权限
        hr_group.permissions.add(*existing_hr_permissions)
        
        # Employee组权限
        employee_group, created = Group.objects.get_or_create(name='Employee')
        # 重置现有权限
        employee_group.permissions.clear()
        
        # Employee权限codename列表
        employee_permission_codenames = [
            'view_employee',
            'view_attendance',
            'view_performance',
            'view_userprofile',
        ]
        
        # 获取所有存在的权限
        existing_employee_permissions = Permission.objects.filter(
            Q(codename__in=employee_permission_codenames)
        )
        # 设置Employee组权限
        employee_group.permissions.add(*existing_employee_permissions)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'date_joined')
    list_filter = ('department', 'date_joined')
    search_fields = ('name', 'email')