from django.shortcuts import render

def home(request):
    context = {
        'title': 'Gwiternz',
        'tagline': 'Run, build and grow with confidence.',
        'description': 'Gwiternz delivers project solutions, infrastructure, IT, outsourcing and advisory — the expertise your business needs, exactly when you need it.',
        'trust_badges': [
            'End-to-end delivery',
            'Senior expertise',
            'Kenya-based',
        ],
        'services': [
            {
                'number': '01',
                'title': 'Project Solutions',
                'description': 'End-to-end project management and delivery that keep complex initiatives on time and on budget.',
            },
            {
                'number': '02',
                'title': 'Infrastructure',
                'description': 'Resilient networks, servers, cloud, power and connectivity, designed, secured and managed so your business never skips a beat.',
            },
            {
                'number': '03',
                'title': 'IT Services',
                'description': 'From responsive support to web, mobile, software and AI, your complete technology partner.',
            },
            {
                'number': '04',
                'title': 'Outsourcing',
                'description': 'Vetted staff outsourcing, placements and contracted resources, the right skills, exactly when you need them.',
            },
            {
                'number': '05',
                'title': 'Advisory',
                'description': 'Strategic consulting and advisory that turn technology decisions into measurable business advantage.',
            },
        ],
        'value_props': [
            {
                'title': 'One partner, five disciplines',
                'description': 'Project solutions, infrastructure, IT, outsourcing and advisory under a single accountable roof, with no juggling of vendors.',
            },
            {
                'title': 'Senior, vetted expertise',
                'description': 'Experienced professionals matched to your needs, so you get the right skills instead of guesswork.',
            },
            {
                'title': 'Right-sized for your stage',
                'description': 'Engagements scaled to fit startups and growing businesses alike, so you only pay for what you need.',
            },
            {
                'title': 'Accountable delivery',
                'description': 'Clear scope, governance and milestones mean work is delivered on time, on budget and to standard.',
            },
            {
                'title': 'Local knowledge',
                'description': 'A Nairobi-based team that understands the Kenyan market, regulations and business context.',
            },
            {
                'title': 'Responsive support',
                'description': 'We stay close after delivery, not just during it, a partner you can reach when it matters.',
            },
        ],
        'process_steps': [
            {'number': '01', 'title': 'Discover', 'description': 'We learn your goals, context and constraints to understand what success looks like.'},
            {'number': '02', 'title': 'Plan', 'description': 'We scope the work, agree the approach and set a clear roadmap with milestones.'},
            {'number': '03', 'title': 'Deliver', 'description': 'We execute with governance and regular check-ins, keeping you informed throughout.'},
            {'number': '04', 'title': 'Support', 'description': 'We stay on as your partner beyond go-live, ready when you need us next.'},
        ],
        'clients': [
            'StarMed Technologies',
            'Ropi Robi Ventures',
            'SalusCare',
            'Tumia',
            'Ten Marketplace',
            'AfixCrypto',
        ],
    }
    return render(request, 'pages/home.html', context)
