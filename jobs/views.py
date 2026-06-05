from django.shortcuts import render, get_object_or_404
from .models import Job


def home(request):
    recent_jobs = Job.objects.filter(is_active=True)[:6]
    total_jobs = Job.objects.filter(is_active=True).count()
    return render(request, "jobs/home.html", {"recent_jobs": recent_jobs, "total_jobs": total_jobs})


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    query = request.GET.get("q", "")
    job_type = request.GET.get("job_type", "")

    if query:
        jobs = jobs.filter(title__icontains=query) | jobs.filter(company__icontains=query) | jobs.filter(location__icontains=query)
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    job_types = Job.JOB_TYPE_CHOICES
    return render(request, "jobs/job_list.html", {
        "jobs": jobs,
        "query": query,
        "job_type": job_type,
        "job_types": job_types,
    })


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    return render(request, "jobs/job_detail.html", {"job": job})
