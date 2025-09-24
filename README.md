# Golden Config Design Job

This repository define custom DesignJob, which provide jinja2 template for creating device Core Router *r1* with assigned Golden Config.

## Structure

```
├── ./__init__.py # neccesery for nautobot to load the job
├── ./jobs
│   ├── ./jobs/gc_design
│   │   ├── ./jobs/gc_design/context
│   │   │   └── ./jobs/gc_design/context/__init__.py # defnition of custom context
│   │   ├── ./jobs/gc_design/designs
│   │   │   └── ./jobs/gc_design/designs/0001.yaml.j2 # custom jinja2 template
│   │   └── ./jobs/gc_design/__init__.py # custom DesignJob definition
│   └── ./jobs/__init__.py # linking all the defined jobs
```
